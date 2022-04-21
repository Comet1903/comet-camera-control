import cv2
import numpy as np
import pyautogui

cv2.namedWindow("Comet Camera Control - CCC") # Create a named window
vc = cv2.VideoCapture(0) # Set camera to use

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read() # read the first frame
else:
    rval = False

while rval:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert to HSV
    mask = cv2.inRange(hsv, (0, 0, 0), (360, 360, 50)) # Set HSV color range

    screen_width, screen_height = pyautogui.size() # Get screen size

    width = mask.shape[1] # Get width of camera
    height = mask.shape[0] # Get height of camera

    ret, thresh = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY) # Threshold image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find contours

    #cv2.drawContours(frame, contours, -1, (0,255,0), 3) # Draw all contours

    if len(contours) != 0:
        c = max(contours, key = cv2.contourArea) # Find largest contour
        x,y,w,h = cv2.boundingRect(c) # Get bounding rectangle

        cv2.drawContours(frame, c, 0, (0,255,0), 3) # Draw contour
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # Draw bounding rectangle around contour

        cursor_pos_x = screen_width*((x+w/2)/width) # Calculate cursor position
        cursor_pos_y = screen_height*((y+h/2)/height) # Calculate cursor position

        print("Set cursor to: x=" + str(cursor_pos_x) + ", y=" + str(cursor_pos_y)) # Print cursor position

        pyautogui.moveTo(cursor_pos_x, cursor_pos_y) # Set cursor position


    cv2.imshow("Comet Camera Control - CCC", frame) # Show image
    rval, frame = vc.read() # Get next frame
    key = cv2.waitKey(20) # Wait for key press
    if key == 27: # If ESC key is pressed
        break # Exit loop

vc.release() # Release camera
cv2.destroyWindow("Comet Camera Control - CCC") # Close window

