# 📹 TikTok Generator : Create vertical compiliation videos
## 📚 Description
A simple script that i made to generate automaticly Tiktok "compiliation of images" videos. Add titles, downloaded images and sounds, and make thousands of videos in minutes !

## 🚀 Features 
- Generate random ready-to-upload Tiktok videos with one command.
- Customize sounds, images in background and opening title videos of the produced videos.
- Option to delete the images used, so you can't have two time an image in different videos.

## 💻 Installation
To install and run TiktokGenerator, you will need to have :
- [Python](https://www.python.org/downloads/)
- [Moviepy package](https://zulko.github.io/moviepy/)
- [PIL package](https://he-arc.github.io/livre-python/pillow/index.html)

*Note* : You also may have to create empty folders used by the script in his location : "Intros", "Sounds", "Images" and "Output".

## 👤 Organization of the repo
The main script is script_compil.py and is in Python. The file script_conseils.py is another test that i made for another format that doesn't work well, so feel free to use it or not.


## 🕹️ Usage
To use the script, simply follow these steps :
### 1) Add images in your main theme
You can choose a specific subreddit for example, and use a tool like [Bulk Downloader For Reddit](https://github.com/aliparlakci/bulk-downloader-for-reddit). Place all the images in a folder "Images" next to the scripts.

*Note :* I suggest you to rename all your images with the same pattern and without spaces with [PowerRename](https://learn.microsoft.com/en-us/windows/powertoys/powerrename) or equivalent.

### 2) Choose opening videos and songs
And place it in appropriate folders ("Intros" and "Sounds" folders). 10 differents songs / titles is a good number. You can make the opening videos on a simple video tool like Capcut.

### 3) Start the program
```
python -m script_compil
```
You will then be prompted to select if you want to delete used images. Enter y or n and let the magic happen.

### 4) Get the videos in the Output folder

## 🖼️ Example
Here is an example of a random generated video with the script :

<img src=".images/demo.gif" height="500">

