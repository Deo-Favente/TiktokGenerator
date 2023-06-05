import os
import random
from moviepy.editor import *

def generate_tiktok_videos(num_videos, delete_files):
    video_folder = "C:/Users/enzod/Desktop/TiktokAuto/Fond_Conseil"  # Chemin vers le dossier contenant les vidéos de fond
    music_folder = "C:/Users/enzod/Desktop/TiktokAuto/Sons"  # Chemin vers le dossier contenant les musiques de fond
    text_folder = "C:/Users/enzod/Desktop/TiktokAuto/Textes"  # Chemin vers le dossier contenant les fichiers texte
    output_folder = "C:/Users/enzod/Desktop/TiktokAuto/Output"  # Chemin vers le dossier de sortie
    font = "C:/Users/enzod/Desktop/TiktokAuto/Fonts/LeagueSpartan-Medium.ttf"  # Chemin vers la police d'écriture

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(num_videos):
        # Sélection aléatoire d'une vidéo de fond
        video_file = random.choice(os.listdir(video_folder))
        video_path = os.path.join(video_folder, video_file)

        # Sélection aléatoire d'une musique de fond
        music_file = random.choice(os.listdir(music_folder))
        music_path = os.path.join(music_folder, music_file)

        # Lecture du fichier texte
        text_file = random.choice(os.listdir(text_folder))
        text_path = os.path.join(text_folder, text_file)

        # Dimensions de la vidéo
        video_width = 720
        video_height = 1280

        # Taille et police du titre
        title_font_size = 30

        # Taille et police du contenu
        content_font_size = 35

        # Lecture du fichier texte
        with open(text_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Extraction du titre et du contenu
        title = lines[0].strip()
        content = [line.strip() for line in lines[1:]]

        # Création de l'image de fond
        background_video = VideoFileClip(video_path)
        background_video = background_video.resize(height=video_height)

        # Création du titre
        title_clip = TextClip(title, fontsize=title_font_size, color='white', font=font, align='center', stroke_color='black', stroke_width=2,
                            size=(video_width - 50, None)).set_position(('center', video_height // 8 - 50)).set_duration(3)

        # Calcul de la taille des zones de texte
        text_height = (video_height - (video_height // 8)) // 4
        text_width = video_width // 2

        # Création des textes de contenu
        content_clips = []

        line_count = 4  # Nombre total de lignes
        line_spacing = (video_height - line_count * text_height) // (line_count + 1) - 75 # Espacement vertical entre les lignes

        for i, text in enumerate(content):
            line = i % line_count
            col = (i // line_count) % 2
            x = col * text_width

            y = (line + 1) * line_spacing + line * text_height + 225
            
            # Diviser le texte en mots
            words = text.split()
            num_words = len(words)
            
            # Créer des sous-listes de mots avec 4 mots chacune
            split_words = [words[j:j+3] for j in range(0, num_words, 3)]
            
            # Joindre les sous-listes de mots avec des retours à la ligne
            lines = [" ".join(sublist) for sublist in split_words]
            text_with_line_breaks = "\n".join(lines)
            
            content_clip = TextClip(text_with_line_breaks, fontsize=content_font_size, color='white', font=font, align='center', stroke_color='black', stroke_width=1.2,
                                    size=(text_width, text_height), method='caption').set_position((x, y)).set_duration(3)

            content_clips.append(content_clip)

        # Composition des clips de texte
        text_clip = CompositeVideoClip([title_clip] + content_clips, size=(video_width, video_height))

        # Superposition du clip de texte sur l'image de fond
        final_clip = CompositeVideoClip([background_video, text_clip])

        # Création de la vidéo finale avec la durée de la vidéo de fond
        final_clip = final_clip.set_duration(background_video.duration)

        # Ajout de la musique de fond
        audio_clip = AudioFileClip(music_path)
        audio_clip = audio_clip.subclip(0, final_clip.duration)
        final_clip = final_clip.set_audio(audio_clip)

        # Sauvegarde de la vidéo générée
        output_path = os.path.join(output_folder, f"tiktok_video_{i}.mp4")
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True, fps=24, bitrate="5000k")

        # Nettoyage des fichiers texte utilisés si spécifié
        if delete_files:
            os.remove(text_path)

    print(f"{num_videos} vidéos TikTok générées avec succès!")

num_videos_to_generate = int(input("Combien de vidéos TikTok souhaitez-vous générer ? "))
delete_files_after_generation = input("Voulez-vous supprimer les fichiers texte utilisés ? (oui/non) ").lower() == "oui"

generate_tiktok_videos(num_videos_to_generate, delete_files_after_generation)
