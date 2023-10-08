# Make sure you have the following packages installed using pip:
#pip install opencv-python
#pip install numpy

import cv2  # Import the OpenCV library for video processing
import numpy as np  # Import NumPy for numerical operations
import csv  # Import the CSV library for file handling

# Load the video
video_path = 'vid3.mp4'  # Change this to your video file path
cap = cv2.VideoCapture(video_path)

# Initialize matrices for time, brightness, and contrast
tiempo_actual = 0  # Initialize current time to 0
intervalo_tiempo = 0.05  # Change this value to the desired time interval (in seconds)
datos_luminosidad_contraste = []  # Initialize an empty list for storing data

while True:
    ret, frame = cap.read()  # Read a frame from the video
    if not ret:
        break

    tiempo_frame = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Current time in seconds

    if tiempo_frame >= tiempo_actual + intervalo_tiempo:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
        luminosidad = np.mean(gray_frame)  # Calculate brightness
        contraste = np.std(gray_frame)  # Calculate contrast

        # Add time, brightness, and contrast with three decimal places
        datos_luminosidad_contraste.append([round(tiempo_actual, 3), round(luminosidad, 3), round(contraste, 3)])

        tiempo_actual += intervalo_tiempo  # Update the current time

# Save brightness and contrast data to a CSV file
with open('datos_luminosidad_contraste.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tiempo (segundos)', 'Luminosidad', 'Contraste'])  # Write headers
    writer.writerows(datos_luminosidad_contraste)  # Write data to the CSV file

cap.release()  # Release resources
