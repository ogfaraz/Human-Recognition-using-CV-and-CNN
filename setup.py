# Import necessary libraries
import shutil  
import os  



if os.path.isdir("image"):
    # If it exists, remove the "image" directory and all its contents
    shutil.rmtree("image")



if os.path.isdir("image_test"):
    # If it exists, remove the "image_test" directory and all its contents
    shutil.rmtree("image_test")



import config  
# Import config module which contains Starting queries.



import collect_image  
# Import collect_image module for collecting training images.



import collect_image_test  
# Import collect_image_test module for collecting test images.



import train  
# Import train module for training the model.



import Real_Time  
# Import Real_Time module for real-time recognition.




print("""                     

            \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTHAT IS ALL!
      \n\n\t\t\t\tYOU CAN RUN python 'Real_Time.py' AGAIN FOR REAL TIME VIDEO AFTER TRAINING
\t\t\t\t\n





    """)
