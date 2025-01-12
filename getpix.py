import cv2
import numpy
#1366x768
img_rgb = cv2.imread("Untitled.jpg",1)
count=0
for i in range(768):
    for j in range(1366):
        #print(type(list(img_rgb[i][j])))
        if list(img_rgb[i][j])==[185,185,185]:
            count+=1
            #print(list(img_rgb[i][j]))
    
print(count)
