# 📹 TikTok Generator : Generate multiples videos with Python
## 📚 Description
A simple script that i made to generate automaticly Tiktok "compiliation of images" videos. Add titles, downloaded images and sounds, and make thousands of videos in minutes !

## 🚀 Features 
- Generate random ready-to-upload Tiktok videos with one command.
- Customize sounds, images in background and main title of the videos.
- Option to delete the images used, so you can't have two time an image in different videos.

## 💻 Installation
To install and run TiktokGenerator, you will need to have :
- [Python](https://www.python.org/downloads/)
- [Moviepy package](https://zulko.github.io/moviepy/)

## 👤 Organization of the repo
The main script is script_compil.py and is in Python. The file script_conseils.py is another test that i made for another format that doesn't work well, so feel free to use it or not.


## 🕹️ Usage
To use the script, simply follow these steps
### 1) Download bulk images in your main theme
You can choose a specific subreddit for example, and use a tool like [Bulk Downloader For Reddit](https://github.com/aliparlakci/bulk-downloader-for-reddit). Place all the images in a folder "Images" next to the scripts.
*Note :* I suggest you to rename all your images with the same pattern and without spaces with (PowerRename)[https://learn.microsoft.com/en-us/windows/powertoys/powerrename] or an equivalent.

### 2) Choose titles and songs
And place it in appropriate folders. 10 differents songs / titles is a good number.

## 3) Start the program
```
python -m script_compil
```
You will then be prompted to select if you want to delete used images. Say yes or no and let the magic happen.

## 🖼️ Example
Here is an example of a random generated video with the script :

<img src=".images/demo.gif" height="500">

