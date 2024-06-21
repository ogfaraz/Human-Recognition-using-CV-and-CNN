
#n , max1, max2, epochs 

import os

# Clear the console screen
os.system("cls")

# Print introductory messages to the console
print("\n\n\t\tBy Faraz Harris & Naveed")
print("\t\t\tIn the First stage, we start by Collecting Image for Train and Test\t\t\t")


print("________________________________________________________________________________")


# Prompt the user to input the number of persons or objects and convert the input to an integer
# 'n' is the number of different categories (e.g., people or objects) for which images will be collected
n = int(input("   How many persons or objects:  "))

# Prompt the user to input the number of training images they want to collect and convert the input to an integer
# 'max1' is the number of images to be collected for training purposes (suggested: 400 images)
max1 = int(input("  How many images do you want for training (400 is best):  "))


# Prompt the user to input the number of testing images they want to collect and convert the input to an integer
# 'max2' is the number of images to be collected for testing purposes (suggested: 200 images)
max2 = int(input("  How many images do you want for testing (200 is best):  "))


# Print another separator line to the console for better readability
print("________________________________________________________________________________")


# Clear the console screen again to prepare for the next stage of input
os.system("cls")


# Prompt the user to input the number of epochs for training the model and convert the input to an integer
# 'epochs' is the number of training iterations for the CNN model
# Higher values (e.g., 10) result in longer but potentially more accurate training, whereas lower values (e.g., 3) result in faster training
epochs = int(input("Enter epochs for training (10 is slower & 3 is faster): "))
