YouTube Downloader
A user-friendly web application to download YouTube videos as MP4 or audio as MP3 files. Built with Flask (Python backend) and HTML/JavaScript (frontend), it features a simple browser interface where users can input a YouTube URL, choose a format (MP4 or MP3), and download the file with a progress bar and status messages.
Legal Disclaimer: Downloading YouTube videos may violate YouTube's Terms of Service unless you have explicit permission from the content owner or the video is licensed for download (e.g., Creative Commons). Use this tool responsibly, such as for your own videos or public domain content. The developer is not responsible for misuse.
Features

Download YouTube videos in MP4 format (up to 720p for reliable performance).
Extract audio from YouTube videos as MP3 files (128kbps).
Clean, responsive web interface with real-time progress updates.
Automatic cleanup of downloaded files older than 24 hours.
Supports standard YouTube URLs (e.g., https://www.youtube.com/watch?v=... or https://youtu.be/...).

Prerequisites

Operating System: Windows 10/11 (tested on Windows 10, version 10.0.22621.4317).
Python: Version 3.13 with the Python Launcher (py command).
FFmpeg: Installed and added to system PATH for MP3 conversion.
Terminal: PowerShell or Command Prompt.
Internet Connection: Stable connection for downloading videos.

Installation

Set Up the Project Folder:

Create a folder at C:\Users\YourUsername\youtube-downloader.
Ensure the following structure:youtube-downloader\
├── public\
│   └── index.html      # Frontend HTML and JavaScript
├── venv\               # Python virtual environment
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── README.md           # This file




Install FFmpeg:

Download the FFmpeg binary from gyan.dev (e.g., ffmpeg-release-full.7z).
Extract to C:\ffmpeg\ffmpeg-release-full using 7-Zip.
Add C:\ffmpeg\ffmpeg-release-full\bin to your system PATH:
Press Win + R, type sysdm.cpl, go to Advanced > Environment Variables.
Edit "Path" under System variables, add the bin path, and save.


Verify in PowerShell:ffmpeg -version


Expected: ffmpeg version N-120025-gf67ca10f2e-20250624 or similar.




Set Up Python Virtual Environment:

Open PowerShell and navigate to the project folder:cd C:\Users\YourUsername\youtube-downloader


Create a virtual environment:py -m venv venv


Activate it:.\venv\Scripts\Activate.ps1


If you get a script execution error, run:Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


Type Y to confirm.






Install Python Dependencies:

Ensure requirements.txt contains:flask==3.0.3
yt-dlp==2024.10.22
ffmpeg-python==0.2.0
flask-cors==5.0.0


Install dependencies:pip install -r requirements.txt


Keep yt-dlp updated:pip install --upgrade yt-dlp




Verify Installation:

Check Python and pip:py --version
pip --version


Expected: Python 3.13.x, pip 25.1.1.


Check FFmpeg:ffmpeg -version


Check dependencies:pip list


Look for flask, yt-dlp, ffmpeg-python, flask-cors.


Verify folder structure in File Explorer.



Usage

Run the Application:

In PowerShell (with (venv) active):cd C:\Users\YourUsername\youtube-downloader
.\venv\Scripts\Activate.ps1
py app.py


Expected output:* Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)




Access the Web Interface:

Open a browser (e.g., Chrome, Edge) and go to http://localhost:3000.
Enter a valid YouTube URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ).
Select MP4 for video or MP3 for audio.
Click Download Now to start the download.
Files will save to your default Downloads folder (e.g., C:\Users\YourUsername\Downloads).


Verify Downloads:

Check C:\Users\YourUsername\Downloads for files (e.g., Video_Title.mp4 or Video_Title.mp3).
Play the files to confirm they work correctly.



Troubleshooting

Port Conflict:

If port 3000 is in use, edit app.py to change port=3000 to port=5000:app.run(host='0.0.0.0', port=5000, debug=True)


Update index.html’s fetch URL to http://localhost:5000/download.
Retry py app.py and use http://localhost:5000.


Download Fails:

Check PowerShell for errors (e.g., timeouts, yt-dlp issues).
Update yt-dlp:pip install --upgrade yt-dlp


Ensure a stable internet connection:ping google.com


Check browser console (F12 > Console) for errors.


FFmpeg Errors:

Verify FFmpeg:ffmpeg -version


Re-add C:\ffmpeg\ffmpeg-release-full\bin to PATH if needed.


Files Not Downloading:

Check C:\Users\YourUsername\youtube-downloader\downloads for temporary files.
Disable browser pop-up blockers.



Project Structure
youtube-downloader/
├── public/
│   └── index.html       # Frontend HTML and JavaScript
├── venv/                # Python virtual environment
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── downloads/           # Temporary folder for downloaded files (created automatically)

Legal Disclaimer
This tool is for educational purposes only. Respect YouTube’s Terms of Service and only download content you have permission to access. The developer is not responsible for any misuse of this application.
Contributing
Contributions are welcome! Fork the project, make improvements, and submit pull requests. Report issues or suggest features by contacting the project maintainer.
Acknowledgments

Built with Flask, yt-dlp, and FFmpeg.
Tested on Windows 10 with Python 3.13 as of June 25, 2025.
