# Importing necessary libraries
import cv2  
from keras import Sequential  
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten  
import keras  
import numpy as np  
import glob  
from config import n, max1, max2, epochs  


print("\n\t\t_________________+++++++ LOADING... +++++++_______________\t\t\n")


names = []

# Use glob to find all directories under "image"
a = glob.glob("image/*")


# Join the list into a single string and then split it into a list of directories
b = " ".join(a).split(" ")

# Extract and append the directory names to the 'names' list
for i in b:
    names.append(i.split('\\')[1])



# Assign class names based on the directory names
class_names = names


# Initialize lists to store training and testing data and labels
train = []
labels = []
X_test = []
y_test = []



# Loop through each class name to read training images and their labels
for num, name in enumerate(names):
    for i in range(1, max1):
        a = cv2.imread(f"image/{name}/{name}.{i}.jpg")  # Read the image
        labels.append(num)  
        train.append(a)  



# Loop through each class name to read testing images and their labels
for num, name in enumerate(names):
    for i in range(1, max2):
        a = cv2.imread(f"image_test/{name}/{name}.{i}.jpg")  
        y_test.append(num)  # label corresponding to the class
        X_test.append(a)  # Append the image



# Convert lists to NumPy arrays for processing
X_test = np.array(X_test)
y_test = np.array(y_test)
train = np.array(train)
labels = np.array(labels)



# Normalize the images to have values between 0 and 1
X_test = X_test / 255.0
train = train / 255.0


# Print the first few and last few labels to check the data
print(labels[:5])
print(labels[193:])



# Create a Sequential model
model = Sequential()

# Add a 2D convolutional layer with 128 filters, a kernel size of 3x3, ReLU activation, and input shape of 128x128x3
model.add(Conv2D(128, (3, 3), activation="relu", input_shape=(128, 128, 3)))

# This layer reduces the spatial dimensions (height and width) of the feature maps by taking the maximum value in each 2x2 block
model.add(MaxPooling2D(2, 2))


# This layer further detects features with its 256 filters in the feature maps produced by the previous layer
model.add(Conv2D(256, (3, 3), activation="relu"))
model.add(MaxPooling2D(2, 2))

# Add another 2D convolutional layer with 256 filters and a kernel size of 3x3 with ReLU activation
model.add(Conv2D(256, (3, 3), activation="relu"))
model.add(MaxPooling2D(2, 2))

# Add a flatten layer to convert the 2D feature maps into a 1D feature vector, necessary before passing the data to fully connected (dense) layers
model.add(Flatten())

# Add a fully connected (dense) layer with 128 units. This layer learns to interpret the features extracted by the convolutional layers
model.add(Dense(128, activation="relu"))

# Add an output layer with 'n' units (one for each class) and softmax activation
model.add(Dense(n, activation="sigmoid"))


# The optimizer updates the model weights to minimize the loss function
# SparseCategoricalCrossentropy because the labels are integers
model.compile(optimizer="adam", loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False), metrics=["acc"])


model.fit(train, labels, epochs=epochs, validation_data=(X_test, y_test))

# Save the trained model to a file
model.save("model.h5")


score = model.evaluate(X_test, y_test)

# Print the total accuracy of the model
print("Total Accuracy: ", score[1])
print("Successful...")


print("\n\t+++++++ Please Run python Real_Time.py ++++++++")


'''''''''
Conv2D layers: Apply convolutional operations to the input data.
MaxPooling2D layers: Reduce the spatial dimensions of the input data.
Flatten layer: Flatten the input data to a single dimension.
Dense layers: Fully connected layers for classification.

Activation functions:
"relu" (Rectified Linear Unit) activation function for hidden layers.
"softmax" activation function for the output layer to output probabilities for each class.'''''''''
