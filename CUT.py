import cv2 as cv
orignal = cv.imread('Hsample.jpg')
slid = orignal[230:310, 240:430]
cv.imshow("Original Image", orignal)
cv.imshow("Sliced Image", slid)
cv.waitkey(0)
