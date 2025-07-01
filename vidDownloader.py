from yt_dlp import YoutubeDL

def download_video(url):
    options = {
        'format': 'bv[height=1080]+ba/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

def download_audio(url):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

def main():
    print("What would you like to do?")
    print("1 - Download 1080p video")
    print("2 - Download MP3 audio")
    choice = input("Enter 1 or 2: ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice. Please run the script again.")
        return

    url = input("Enter the YouTube URL: ").strip()

    if choice == '1':
        download_video(url)
    else:
        download_audio(url)

    print("\n✅ Download completed. Script finished.")  

if __name__ == "__main__":
    main()



""" Instructions | Note to Self """
# type to get into venv: python -m venv venv
# then: .\venv\Scripts\activate 

# the second "venv" is the name of the folder and so whatever that's name is, goes for the "\venv\" in the second command


# pip install yt-dlp

# type "deactivate" to turn off the venv

# Check if in venv with: python -c "import sys; print(sys.prefix)"