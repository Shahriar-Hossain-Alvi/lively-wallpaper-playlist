import subprocess
import time
import os
import random

# --- CONFIGURATION ---
# Path to your main Lively executable
LIVELY_PATH = r"E:\Softwares (Installation Area)\Lively Wallpaper\Lively.exe"
# Folder containing your video wallpapers
WALLPAPER_FOLDER = r"G:\Pictures\Walpapers\Live Walpapers"
# Time in seconds between switches (e.g., 60 for 1 minute)
INTERVAL = 600


def set_wallpaper(file_path):
    """Sends the setwp command to the main Lively executable."""
    try:
        # Note: We use 'setwp' as the argument passed to the main exe
        subprocess.run([LIVELY_PATH, "setwp", "--file", file_path], check=True)
        # print(f"✅ Switched to: {os.path.basename(file_path)}")
    except Exception as e:
        # print(f"❌ Error: {e}")
        pass


def start_slideshow():
    # Initial delay to let windows and lively start porperly
    time.sleep(60)

    # Supported video/image formats
    valid_exts = ('.mp4', '.mov', '.avi', '.mkv', '.gif', '.wmv')

    while True:
        # check drive
        if not os.path.exists(WALLPAPER_FOLDER):
            time.sleep(10)
            continue

        videos = [os.path.join(WALLPAPER_FOLDER, f) for f in os.listdir(WALLPAPER_FOLDER)
                  if f.lower().endswith(valid_exts)]

        if not videos:
            time.sleep(10)
            continue

    # print(f"🚀 Playlist started. Changing every {INTERVAL} seconds.")
        random.shuffle(videos)

        for video in videos:
            set_wallpaper(video)
            time.sleep(INTERVAL)


if __name__ == "__main__":
    start_slideshow()
