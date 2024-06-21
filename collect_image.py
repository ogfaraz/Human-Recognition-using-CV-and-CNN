import cv2
import numpy as np  
import time  
import os  
from os import path  

import random  # Import the random module to apply data augmentation

from config import n, max1  # Import configuration values


print("__________________________ LOADING... _________________________")


# Create a new directory named "image" to store collected images
os.mkdir("image")


# Loop to collect images for each person or object
for i in range(n):

    os.system("cls")
    print("_______________________________________________________________")


    name = input("Enter Your Name (ONE Word): ")


    print("________________________________________________\n\n")
    print("______________________ LOADING... ________________________")


    cap = cv2.VideoCapture(0)


    input(f"Are you ready to take a picture, {name}?")


    count = 0
    start = True


    while start:

        file_name = f'image/{name}'

        if not path.isdir(file_name):
            os.mkdir(file_name)


        ret, frame = cap.read()
        count += 1


        # Apply random data augmentation techniques to the captured image
        face = cv2.resize(frame, (128, 128))  # Resize the frame


        # Apply random rotation augmentation
        if random.choice([True, False]):

            angle = random.uniform(-15, 15)  # Random rotation angle between -15 to 15 degrees

            M = cv2.getRotationMatrix2D((128 / 2, 128 / 2), angle, 1)  # Rotation matrix

            face = cv2.warpAffine(face, M, (128, 128))  # Apply rotation



        # Apply random horizontal flip augmentation
        if random.choice([True, False]):

            face = cv2.flip(face, 1)  # Horizontal flip


        # Apply random vertical flip augmentation
        if random.choice([True, False]):

            face = cv2.flip(face, 0)  # Vertical flip


        # Apply random up and down shift augmentation
        if random.choice([True, False]):

            shift_x = random.randint(-5, 5)

            shift_y = random.randint(-5, 5)

            M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

            face = cv2.warpAffine(face, M, (128, 128))


        # Save the augmented frame as an image file
        file_name_path = f'{file_name}/{name}.{count}.jpg'

        cv2.imwrite(file_name_path, face)

        # Put the count number on the image and display it
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        # Resize the image for display purposes
        face = cv2.resize(face, (600, 600))

        # Display the image in a window named 'Face Cropper'
        cv2.imshow('Face Cropper', face)

        # Check if the Enter key (key code 13) is pressed or if the required number of images is reached
        if cv2.waitKey(1) == 13 or count == max1:
            start = False

    cap.release()
    cv2.destroyAllWindows()
    os.system("cls")

print("\n\n___________+++++++ Samples Collection Phase Completed!!! +++++++_______________")
