#RoadBot Vision Processing
#Group12 -Nathaniel Jackson, Jerrod Rout, Blake Taylor, Akash Patel
#When run this code will load images of road signs from Campics folder
#and use template matching with frames captured through a video stream.
#If a sign is found in the video feed frame a serial command is sent
#to the arduino instructing the robot to move in a certain direction.

import cv2					# Import OpenCV library
import serial					# Import serial library
import numpy as np                              # Import NP
import matplotlib.pyplot as mtl                 # Import matplotlib
import time                                     # Import time
ser = serial.Serial('COM4', 38400)	        # Set baud rate to 38400; serial communication through COM4 port  	

cap = cv2.VideoCapture(0)			# Read streaming images from webcam					

GO = cv2.imread('Campics/Go.png')	        # Save image of ‘GO’ sign from database as ‘GO’
GO =cv2.cvtColor(GO, cv2.COLOR_BGR2RGB)	        # Reformat from BGR to RGB 
height1, width1, length1 = GO.shape		# Format ‘GO’ image size

LEFT = cv2.imread('Campics/Left.png') 		# Save image of ‘Left’ sign from database as ‘Left’
LEFT =cv2.cvtColor(LEFT, cv2.COLOR_BGR2RGB)	# Reformat from BGR to RGB
height3, width3, length3 = LEFT.shape		# Format ‘Left’ image size	

STOP = cv2.imread('Campics/Stop.png')		# Save image of ‘Stop’ sign from database as ‘Stop’
STOP =cv2.cvtColor(STOP, cv2.COLOR_BGR2RGB)	# Reformat from BGR to RGB
height4, width4, length4 = STOP.shape		# Format ‘Stop’ image size

i=0	# Initialize counter to zero

ser.write('STOP')	# Initialize robot to stop

while(True):				# While loop to check for incoming image data
        ret, frame = cap.read()	        # Capture frame-by-frame
        Feed = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Reformat streaming images from webcam from BGR to RGB

        result1 = cv2.matchTemplate(Feed,GO,cv2.TM_CCOEFF_NORMED) # Perform template match on webcam feed to find ‘GO’ sign
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1) # Sort results by matching probability

        if(max_val1 >=.6):		# Threshold the probability; must be at least 60% matching probability to enter loop
            top_left = max_loc1 	# Copy ‘max_loc1’ into ‘top_left’ variable
            print ('GO')		# Print ‘GO’ to console
            ser.write('GO')		# Send ‘GO’ string to Arduino IDE
            bottom_right = top_left[0] + width1, top_left[1] + height1 # Save position of match into ‘bottom_right’ variable
            cv2.rectangle(Feed,top_left, bottom_right, (200,0,0),2) # Draw rectangle around match
         
        result3 = cv2.matchTemplate(Feed,LEFT,cv2.TM_CCOEFF_NORMED)  # Perform template matching on webcam feed to find ‘LEFT’ sign
        min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3) # Sort results by matching probability

        if(max_val3>=.6): # Threshold the probability; must be at least 60% matching probability to enter loop

            top_left = max_loc3 	# Copy ‘max_loc3’ into ‘top_left’ variable
            print ('LFFT') 		# Print ‘LEFT’ to console
            ser.write('LEFT')	# Send ‘LEFT’ string to Arduino IDE
            bottom_right = top_left[0] + width3, top_left[1] + height3 # Save position of match into ‘bottom_right’ variable
            cv2.rectangle(Feed,top_left, bottom_right, (200,0,0),2)	# Draw rectangle around match
            while (i<=9015000):	# Delay while robot turns 
                i=i+1			# Increment index by 1
            i=0				# Reset index to zero
            ser.write('GO')    	# Send ‘GO’ string to Arduino IDE to resume forward path
                
        result4 = cv2.matchTemplate(Feed,STOP,cv2.TM_CCOEFF_NORMED) # Perform template matching on webcam feed to find ‘LEFT’ sign
        min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4) # Sort results by matching probability


        if(max_val4 >=.6): # Threshold the probability; must be at least 60% matching probability to enter loop
            top_left = max_loc4 # Copy ‘max_loc4’ into ‘top_left’ variable
            print ('STOP') # Print ‘STOP’ to console 
            ser.write('STOP') # Send ‘STOP’ string to Arduino IDE
            bottom_right = top_left[0] + width4, top_left[1] + height4 # Save position of match into ‘bottom_right’ variable
            cv2.rectangle(Feed,top_left, bottom_right, (200,0,0),2) # Draw rectangle around match
            
       
        cv2.imshow('frame',Feed) # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()	# Once program has finished release the capture
cv2.destroyAllWindows()	# Close all display windows


