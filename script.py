import os
import random
from moviepy.editor import *
from moviepy.video.fx.all import crop
from PIL import Image

def recadrer_image(image_path, output_path):
    # Charger l'image
    image = Image.open(image_path)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image.size

    # Calculer le ratio d'aspect d'origine
    ratio_origine = largeur / hauteur

    # Calculer les nouvelles dimensions en maintenant le ratio d'aspect d'origine
    nouvel_hauteur = int(largeur * 16 / 9)

    # Calculer les marges noires supérieure et inférieure
    marge_verticale = (nouvel_hauteur - hauteur) // 2

    # Créer une nouvelle image avec les dimensions finales et un fond noir
    image_finale = Image.new("RGB", (largeur, nouvel_hauteur), (0, 0, 0))

    # Coller l'image d'origine au centre de l'image finale avec les bordures noires
    image_finale.paste(image, (0, marge_verticale))

    # Enregistrer l'image recadrée avec les bordures noires
    image_finale.save(output_path)

def generate_tiktok_videos(num_videos):
    intros_folder = "C:/Users/enzod/Desktop/TiktokAuto/Intros"
    images_folder = "C:/Users/enzod/Desktop/TiktokAuto/Images/LiminalSpace"
    music_folder = "C:/Users/enzod/Desktop/TiktokAuto/Sons"
    output_folder = "C:/Users/enzod/Desktop/TiktokAuto/Output"

    intros = os.listdir(intros_folder)
    images = os.listdir(images_folder)
    music = os.listdir(music_folder)

    for i in range(num_videos):
        intro = random.choice(intros)
        selected_images = random.sample(images, 6)
        bg_music = random.choice(music)

        intro_path = os.path.join(intros_folder, intro)
        image_paths = [os.path.join(images_folder, img) for img in selected_images]
        music_path = os.path.join(music_folder, bg_music)

        clips = []
        #clips.append(VideoFileClip(intro_path))
        for img_path in image_paths:
            # Recadrer l'image
            recadrer_image(img_path, img_path)

            # Charger l'image
            image = ImageClip(img_path, duration=3)
            
            clips.append(image)

        final_clip = concatenate_videoclips(clips, method="compose")
        #final_clip = final_clip.set_audio(AudioFileClip(music_path))
        
        (w, h) = final_clip.size

        crop_width = h * 9/16
        # x1,y1 is the top left corner, and x2, y2 is the lower right corner of the cropped area.

        x1, x2 = (w - crop_width)//2, (w+crop_width)//2
        y1, y2 = 0, h
        final_clip = crop(final_clip, x1=x1, y1=y1, x2=x2, y2=y2)

        output_path = os.path.join(output_folder, f"video_{i+1}.mp4")
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)

        print(f"La vidéo {i+1} a été générée et sauvegardée dans {output_path}")

        # Supprimer les images utilisées
        for img_path in image_paths:
            os.remove(img_path)
            print(f"L'image {img_path} a été supprimée.")

generate_tiktok_videos(1)  # Exemple : générer 5 vidéos TikTok
