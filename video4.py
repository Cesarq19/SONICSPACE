import cv2
import numpy as np
import csv

# Carga el video
video_path = 'vid3.mp4'  # Cambia esto a la ruta de tu video
cap = cv2.VideoCapture(video_path)

# Inicializa matrices para el tiempo, luminosidad y contraste
tiempo_actual = 0
datos_luminosidad_contraste = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    tiempo_frame = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Tiempo actual en segundos

    if tiempo_frame >= tiempo_actual + 1:  # Calcula el promedio cada 1 segundo
        # Convierte el fotograma a escala de grises
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calcula la luminosidad
        luminosidad = np.mean(gray_frame)

        # Calcula el contraste
        contraste = np.std(gray_frame)

        # Agrega el tiempo, luminosidad y contraste con tres decimales
        datos_luminosidad_contraste.append([round(tiempo_actual, 3), round(luminosidad, 3), round(contraste, 3)])

        # Actualiza el tiempo actual
        tiempo_actual += 1

# Guarda los datos de luminosidad y contraste en un archivo CSV
with open('datos_luminosidad_contraste.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tiempo (segundos)', 'Luminosidad', 'Contraste'])
    writer.writerows(datos_luminosidad_contraste)

# Libera los recursos
cap.release()
