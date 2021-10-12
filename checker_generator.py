import cv2 as cv
import numpy as np

image = np.zeros((1024,1024))

for i in range(256):
    print(image)
    filename = "image/checker_" + str(i) + ".png"
    cv.namedWindow("polarCGH", cv.WINDOW_NORMAL)   
    cv.imwrite(filename,image)
    cv.imshow("image",image)
    
    image += 1