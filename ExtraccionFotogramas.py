import cv2
import numpy as np
import os

# Directorio donde se encuentran los videos
video_directory = 'videos'

# Directorio donde se guardarán los fotogramas
frames_directory = 'Fotogramas'

# Abre cada video en el directorio
for video_filename in os.listdir(video_directory):
    if video_filename.endswith("vid2.mp4"):
        video_path = os.path.join(video_directory, video_filename)
        cap = cv2.VideoCapture(video_path)

        # Asegúrate de que se haya abierto el video correctamente
        if not cap.isOpened():
            continue

        # Crea el directorio para guardar los fotogramas
        os.makedirs(os.path.join(frames_directory, video_filename), exist_ok=True)

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convierte el fotograma a escala de grises
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Calcula la luminosidad promedio del fotograma
            luminosity = np.mean(gray_frame)

            # Puedes hacer más aquí, como guardar el fotograma o procesar la luminosidad

            # Guarda el fotograma en el directorio de fotogramas
            frame_filename = os.path.join(frames_directory, video_filename, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, gray_frame)

            frame_count += 1

        cap.release()

print("Proceso de extracción de fotogramas completado.")
