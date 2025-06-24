from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import yt_dlp
import ffmpeg
import os
import re
import time

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

# Create downloads directory if it doesn't exist
DOWNLOADS_DIR = os.path.join(os.getcwd(), 'downloads')
if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')
    format = data.get('format')

    # Validate URL
    youtube_regex = r'^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)[a-zA-Z0-9_-]{11}'
    if not url or not re.match(youtube_regex, url):
        return jsonify({'success': False, 'message': 'Invalid YouTube URL'}), 400

    try:
        # Get video info
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = re.sub(r'[^\w\s-]', '_', info['title'])[:50]  # Sanitize title

        output_file = os.path.join(DOWNLOADS_DIR, f"{video_title}.{format}")
        download_url = f"http://localhost:3000/downloads/{video_title}.{format}"

        if format == 'mp4':
            # Download video
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': output_file,
                'merge_output_format': 'mp4',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        elif format == 'mp3':
            # Download audio and convert to MP3
            temp_file = os.path.join(DOWNLOADS_DIR, f"{video_title}.webm")
            ydl_opts = {
                'format': 'bestaudio[ext=webm]/bestaudio',
                'outtmpl': temp_file,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # Convert to MP3
            stream = ffmpeg.input(temp_file)
            stream = ffmpeg.output(stream, output_file, format='mp3', ab='128k')
            ffmpeg.run(stream)
            os.remove(temp_file)  # Clean up temporary file

        else:
            return jsonify({'success': False, 'message': 'Unsupported format'}), 400

        return jsonify({
            'success': True,
            'downloadUrl': download_url,
            'filename': f"{video_title}.{format}"
        })

    except Exception as e:
        return jsonify({'success': False, 'message': f'Download failed: {str(e)}'}), 500

@app.route('/downloads/<path:filename>')
def serve_download(filename):
    return send_from_directory(DOWNLOADS_DIR, filename)

# Clean up old files (older than 24 hours)
def cleanup_downloads():
    while True:
        for filename in os.listdir(DOWNLOADS_DIR):
            file_path = os.path.join(DOWNLOADS_DIR, filename)
            if os.path.isfile(file_path):
                file_age = time.time() - os.path.getmtime(file_path)
                if file_age > 24 * 60 * 60:  # 24 hours
                    os.remove(file_path)
        time.sleep(60 * 60)  # Check every hour

if __name__ == '__main__':
    import threading
    cleanup_thread = threading.Thread(target=cleanup_downloads, daemon=True)
    cleanup_thread.start()
    app.run(host='0.0.0.0', port=3000, debug=True)