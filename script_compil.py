# --------------------------------------------------------------------
# Description: Ce script permet de générer des vidéos TikTok à partir
# d'images et de sons aléatoires.
# Auteur : Enzo Dubix
# --------------------------------------------------------------------

# Imports
import os
import random
from moviepy.editor import *
from moviepy.video.fx.all import crop
from PIL import Image

intros_folder = "C:/Users/enzod/Desktop/TiktokAuto/Intros"
images_folder = "C:/Users/enzod/Desktop/TiktokAuto/LiminalSpace"
music_folder = "C:/Users/enzod/Desktop/TiktokAuto/Sons"
output_folder = "C:/Users/enzod/Desktop/TiktokAuto/Output"

def recadrer_image(image_path, output_path):
    # Charger l'image
    image = Image.open(image_path)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image.size

    # Calculer les nouvelles dimensions en maintenant le rapport d'aspect 9:16
    nouvel_hauteur = int(largeur * 16 / 9)

    # Calculer les marges noires supérieure et inférieure
    marge_verticale = int((nouvel_hauteur - hauteur) / 2)

    # Créer une nouvelle image avec les dimensions finales et un fond noir
    image_finale = Image.new("RGB", (largeur, nouvel_hauteur), (0, 0, 0))

    # Calculer les coordonnées du coin supérieur gauche pour coller l'image d'origine
    coin_sup_gauche = (0, marge_verticale)

    # Coller l'image d'origine sur l'image finale avec les bordures noires
    image_finale.paste(image, coin_sup_gauche)

    # Enregistrer l'image recadrée avec les bordures noires
    image_finale.save(output_path)

def generate_tiktok_videos(num_videos, delete_images):

    intros = os.listdir(intros_folder)
    images = os.listdir(images_folder)
    music = os.listdir(music_folder)

    for i in range(num_videos):
        # Sélectionner une introduction aléatoire
        intro = random.choice(intros)

        # Sélectionner 6 images aléatoires
        selected_images = random.sample(images, 6)

        # Sélectionner une musique de fond aléatoire
        bg_music = random.choice(music)
        
        print(f"Intro selectionnée : {intro}")
        print(f"Images selectionnées : {selected_images}")
        print(f"Musique selectionnée : {bg_music}")

        # Chemins des fichiers
        intro_path = os.path.join(intros_folder, intro)
        image_paths = [os.path.join(images_folder, img) for img in selected_images]
        music_path = os.path.join(music_folder, bg_music)

        clips = []
        
        # Redimensionner l'introduction pour correspondre aux dimensions des images
        intro = VideoFileClip(intro_path)
        
        for img_path in image_paths:
            # Recadrer l'image
            recadrer_image(img_path, img_path)

            # Charger l'image et créer un clip vidéo de 3 secondes
            image = ImageClip(img_path, duration=3)
            
            # Redimensionner l'image pour correspondre aux dimensions de l'introduction
            image = image.resize(intro.size)
            
            clips.append(image)

        # Concaténer les clips vidéo pour former le clip final
        final_clip = concatenate_videoclips([intro] + clips, method="compose")
        
        # Ajouter la musique de fond au clip final
        final_clip = final_clip.set_audio(AudioFileClip(music_path))

        """
        # Redimensionner et recadrer le clip final au ratio 16:9
        (w, h) = final_clip.size
        crop_width = h * 9 / 16
        x1, x2 = (w - crop_width) // 2, (w + crop_width) // 2
        y1, y2 = 0, h
        final_clip = crop(final_clip, x1=x1, y1=y1, x2=x2, y2=y2)
        """
        
        # Définir le chemin de sortie du fichier vidéo
        # Récupération du maximum de l'index des fichiers de sortie
        max_index = os.listdir(output_folder)
        max_index = [int(i.split("_")[1].split(".")[0]) for i in max_index]
        max_index = max(max_index) if max_index else 0
        # Chemin de sortie du fichier vidéo
        output_path = os.path.join(output_folder, f"video_{max_index + 1}.mp4")

        # Écrire le clip final dans un fichier vidéo avec les codecs appropriés et une fréquence d'images de 24 fps
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)

        print(f"La vidéo {i+1} a été générée et sauvegardée dans {output_path}")
        print(f"Nombre d'images restantes : {len(images) - 6}, soit environ {round((len(images) - 6) / 6)} vidéos.")

        # Supprimer les images utilisées
        if delete_images == "y":
            for img_path in image_paths:
                os.remove(img_path)
                print(f"L'image {img_path} a été supprimée.")

# Script de test
'''
for i in range(5):
    random_image = random.choice(os.listdir(images_folder))
    recadrer_image(os.path.join(images_folder, random_image), f"C:/Users/enzod/Desktop/TiktokAuto/Output/test{i}.jpg")
'''

# Demander le nombre de vidéos à générer et si les images utilisées doivent être supprimées
num_videos = int(input("Combien de vidéos voulez-vous générer ? "))
delete_images = input("Supprimer les images utilisées ? (y/n) ")

# Appeler la fonction pour générer les vidéos TikTok
generate_tiktok_videos(num_videos, delete_images)
