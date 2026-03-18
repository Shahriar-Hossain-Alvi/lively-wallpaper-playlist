# Lively Wallpaper Playlist
- This scripts will let you use multiple live wallpaper as a playlist (like the slideshow in wallpapers) using lively wallpaper app in windows. 

# How to use
- Install lively wallpaper app
- Download and store video wallpapers in a separate folder
- Clone this repository and open it in code editor
- In `LIVELY_PATH` set your lively wallpaper installation path
- in `WALLPAPER_FOLDER` set your downloaded video folders path
- Optional: Change `INTERVAL` to your desired time(seconds) to go to the next wallpaper
- Optional: Change `time.sleep(60)` to your desired time(seconds) to set the start time of playlist after boot 
- save the file
- Now press `win+R` to open run dialogue box
- type this command `shell:startup` and press enter. It'll open the startup application folder
- In the startup folder, right click mouse button and create a new shortcut and set the path of the `lively_playlist.pyw` file.
- give a name eg: Lively playlist to the shortcut
- Now this will run automatically everytime windows starts (Startup on windows must be enabled for lively wallpaper)
- 
