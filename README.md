# 🎵 YouTube Downloader Script (yt-dlp)

A command-line tool that lets you download **1080p videos** or **MP3 audio** from YouTube using `yt-dlp`.

---

## 🎯 What It Does

- Prompts the user to choose:
  1. Download a 1080p video  
  2. Extract MP3 audio
- Asks for a YouTube URL  
- Downloads and merges video/audio with `ffmpeg`  
- Saves the result in the current working directory

---

## ▶️ How to Use

1. **Install FFmpeg and add it to PATH**  
   - Go to: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)  
   - Download:
     ```
     ffmpeg-release-essentials.zip
     ```
   - Extract to:
     ```
     C:\ffmpeg
     ```
   - Add this to your system PATH:
     ```
     C:\ffmpeg\bin
     ```

2. **To auto-activate venv in VS Code**, run this once:

   ```bash
   python -m venv .venv

   pip install yt-dlp
   ```
---
## Additional Notes

1. Activate your virtual environment (each time you work on the project):

    ```bash
    .\.venv\Scripts\activate
    ```

2. Run the script:

    ```bash
    python vidDownloader.py
    ```

3. Deactivate Virtual Enviroment:

    ```
    deactivate
    ```

4. Double check if currently in venv:

    ```
    python -c "import sys; print(sys.prefix)"
    ```