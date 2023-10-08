#pip install opencv-python
#pip install numpy
import cv2  # Import the OpenCV library for video processing
import numpy as np  # Import NumPy for numerical operations
import os  # Import the OS library for file and directory operations

# Directory where the videos are located
video_directory = 'videos'

# Directory where the frames will be saved
frames_directory = 'Frames'

# Open each video in the directory
for video_filename in os.listdir(video_directory):
    if video_filename.endswith(".mp4"):  # Check if the file is an MP4 video
        video_path = os.path.join(video_directory, video_filename)
        cap = cv2.VideoCapture(video_path)

        # Make sure the video is opened correctly
        if not cap.isOpened():
            continue

        # Create a directory to save the frames
        os.makedirs(os.path.join(frames_directory, video_filename), exist_ok=True)

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Calculate the average luminosity of the frame
            luminosity = np.mean(gray_frame)

            # You can do more here, such as saving the frame or processing the luminosity

            # Save the frame in the frames directory
            frame_filename = os.path.join(frames_directory, video_filename, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, gray_frame)

            frame_count += 1

        cap.release()

print("Frame extraction process completed.")
