# Importing necessary libraries
import cv2  #
import numpy as np  
import time  
import os  
from os import path  
import glob  
from config import n, max2  


names = []

# Use glob to find all directories under "image"
a = glob.glob("image/*")


# Join the list into a single string and then split it into a list of directories
b = " ".join(a).split(" ")

# Extract and append the directory names to the 'names' list
for i in b:
    names.append(i.split('\\')[1])



input("\t\t\n\n This Phase Collects Data For IMAGE TEST  \n Press Enter To Continue...")



os.mkdir("image_test")


# Loop to collect test images for each person or object
for i in range(n):

    # Get the name of the person or object from the 'names' list
    name = names[i]
    print("__________loading________________")
    
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    
    input(f"Are you ready to take a picture, {name}?")
    
    
    count = 0
    start = True
    
    # Start capturing images
    while start:

        # Define the directory path to save images
        file_name = f'image_test/{name}'

        
        if not path.isdir(file_name):
            os.mkdir(file_name)

        # Capture a frame from the webcam
        ret, frame = cap.read()
        
        
        count += 1
        
        
        face = cv2.resize(frame, (128, 128))

        # Define the full path to save the image file
        file_name_path = f'{file_name}/{name}.{count}.jpg'
        
        # Save the resized frame as an image file
        cv2.imwrite(file_name_path, face)

        # Put the count number on the cam and display it
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        
        # Resize the image for display purposes
        face = cv2.resize(face, (600, 600))
        
        # Display the image in a window named 'Face Cropper'
        cv2.imshow('Face Cropper', face)

        # Check if the Enter key (key code 13) is pressed or if the required number of images is reached
        if cv2.waitKey(1) == 13 or count == max2:
            start = False

    # Release the webcam
    cap.release()
    
    
    cv2.destroyAllWindows()
    
    
    os.system("cls")


print("Test Samples Collection is Complete!")
print("\n\n\n______________+++++ Successfully collected images +++++_____________\n\n\n")


time.sleep(1)
