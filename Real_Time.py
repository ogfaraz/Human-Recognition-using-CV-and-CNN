from keras.models import load_model  
import glob  
import cv2  
import numpy as np  
import os  


print("______________________++++++ LOADING... ++++++_____________________")



# Load names from the directories under the "image" directory
names = []

a = glob.glob("image/*")

b = " ".join(a).split(" ")


for i in b:
    names.append(i.split('\\')[1])


# Load the pre-trained model from the file 'model.h5'
model = load_model("model.h5")


os.system("cls")


print("\t\t\n______________________ Starting Real Time Recognition .... ______________________\t\t\n")




# Initialize the webcam
cap = cv2.VideoCapture(0)


# Start an infinite loop to capture video frames in real-time
while True:

    # Read a frame from the webcam
    ret, frame = cap.read()
    


    # Convert the frame to grayscale and detect faces using Haar Cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    


    for (x, y, w, h) in faces:
        
        # Extract the detected face from the frame
        face = frame[y:y+h, x:x+w]
        

        # Resize the face to 128x128 pixels
        face_resized = cv2.resize(face, (128, 128))
        


        # Predict the name using the model
        prediction = model.predict(face_resized.reshape(1, 128, 128, 3))
        
        predicted_class = np.argmax(prediction)
        
        predicted_name = names[predicted_class]
        


        # Draw a rectangle around the detected face and display the name
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.putText(frame, predicted_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    # Resize the frame for display purposes
    frame_resized = cv2.resize(frame, (500, 500))


    # Display the video feed with detections
    cv2.imshow("Real Time Recognition", frame_resized)


    # Break the loop if the Enter key is pressed
    if cv2.waitKey(1) == 13:
        break


cap.release()
cv2.destroyAllWindows()
