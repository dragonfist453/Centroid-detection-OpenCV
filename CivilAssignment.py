'''
This is a project for finding centroid of a given set of shapes on a white background with help of readymade opencv function
Done as part of experiental learning component in the subject "Elements of civil engineering and mechanics"
By Ambu Karthik 1RV18CS019 J CSE 
Year - 2019
'''

import cv2  # OpenCV2 library
import numpy as np   #Numpy library for mathematical and array manipulations

imname = raw_input("Enter the image name with extension provided : ") # Takes name of image from user to find the centroid of

image1 = cv2.imread(imname) # Reads the image and stores in image array
image = cv2.bitwise_not(image1) # Inverted image for thresholding and contouring

height, width, channels =image1.shape # Returns the height, width and the number of channels in the shape

imgray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Converts the given RGB image to grayscale
ret,thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY) # Thresholds and converts all the colour values to binary only (i.e. Black or White)
image2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # Finds all the closed shapes (called contours) in the image

for cnt in contours:

	M = cv2.moments(cnt) # Finding moments of the contour
	cx = int(M['m10']/M['m00']) # X-coordinate of centroid
	cy = int(M['m01']/M['m00']) # Y-coordinate of centroid

	# Coordinates strings	
	coordinates1 = 'The coordinates of centroid of '   
	coordinates2 = 'the surface is ('+str(cx)+','+str(cy)+')'	

	cv2.circle(image1,(cx,cy),1,(255,255,255),2) # Draws a circle with a small radius which appears as a dot

	# Height and Width strings
	heightstr = 'Height : '+str(height)
	widthstr = 'Width : '+str(width)

	# Text insertion commands
	cv2.putText(image1,coordinates2,(cx-100,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),1)	
	cv2.putText(image1,coordinates1,(cx-120,cy-40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),1)
	cv2.putText(image1,heightstr,(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
	cv2.putText(image1,widthstr,(0,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)

cv2.imshow(imname,image1) # Shows the final processed image containing required data 

cv2.waitKey(0)
cv2.destroyAllWindows()
