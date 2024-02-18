import cv2
import os
import time

folder_path = './captureImages'
os.makedirs(folder_path, exist_ok=True)

# Get the list of files in the folder
files_list = os.listdir(folder_path)

# Count the number of files
num_files = len(files_list)
labels = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         '0','1','2','3','4','5','6','7','8','9',
         'call me','check, please','dislike','good job','goodluck','hang lose','high five','hole','i love you','loser','peace','power to','shocker', 'talk to my hand', 'you']
start_time = None
label_index = 0
timer = 1.5
max_image = 10
# Initialize the camera
camera = cv2.VideoCapture(1)  # change the number base on camera numbers starts with 0

print("Please pose {} and press enter to start".format(labels[0]))

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Display the frame
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == 13:  # Capture an image
        start_time = time.time()  # Start the timer
        print("Timer started.")

    if start_time is not None and time.time() - start_time >= timer: 
        # increment base on the number inside the folder path 
        num_files += 1

        # break when finished 
        if num_files > len(labels) * max_image:
            print("Congratulations!! Image dataset is now completed!!")
            break

        # get current label index 
        current_pose_index = labels[label_index]

        # max_image per model in labels array
        if num_files % max_image == 0:
            label_index += 1

        # Save the captured image
        image_file_name = '{}-{}.jpg'.format(current_pose_index,num_files)
        image_path = os.path.join(folder_path, image_file_name)
        cv2.imwrite(image_path, frame)
        print("{} SAVE SUCCESSFULY!".format(image_file_name))
        # reset timer 
        start_time = None

        # proceed until it reaches the max_image 
        if num_files % max_image != 0:
            start_time = time.time()
        else:
            print("NOW! PLEASE MAKE A POSE OF {}".format(labels[label_index]))
            print("PRESS ENTER TO CONTINUE CAPTURING")
        
    elif cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit capturing images
        break

# Release the camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()
