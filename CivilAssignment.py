'''
This is a project for finding centroid of a given set of shapes on a white background with help of readymade opencv function and also by seperating shapes and finding individual centroids of each simple shape to find the perfect centroid of the given surface. 
Done by Ambu Karthik of J section with USN 1RV18CS019.
Done as part of experiental learning component in the subject "Elements of civil engineering and mechanics" in the year 2019
'''

import cv2  # OpenCV2 library
import numpy as np   #Numpy library for mathematical and array manipulations	

imname = raw_input("Enter the image name with extension provided : ") # Takes name of image from user to find the centroid of
image = cv2.imread(imname) # Reads the image and stores in image array

cv2.imshow(imname,image)  

cv2.waitKey(0)

cv2.DestroyAllWindows()
