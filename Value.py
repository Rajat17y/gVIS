import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("Untitled.jpg")
intest = img[117:151,884:981]
words = pytesseract.image_to_string(intest)
print(words)
cv2.imshow("LOL",intest)
cv2.waitKey(0)
