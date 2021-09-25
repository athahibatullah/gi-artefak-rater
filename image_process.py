# Import required packages
import sys
sys.path.insert(1,'package\Lib\site-packages') #to get all the package

 # importing modules
import cv2
import pytesseract

path_to_tesseract = '../Tesseract-OCR/tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

# reading image using opencv

img = cv2.imread('sample/Arte Ganyu 1.png')
bigger = cv2.resize(img, (600, 800))

# Convert the image to gray scale
gray = cv2.cvtColor(bigger, cv2.COLOR_BGR2GRAY)
 
# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
# Specify structure shape and kernel size.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 11))
 
# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
 
# Creating a copy of image
im2 = bigger.copy()

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()
 

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]
     
    # Open the file in append mode
    file = open("recognized.txt", "a")
     
    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
    print(text)
    # Appending the text into file
    file.write(text)
    file.write("\n")
     
    # Close the file
    file.close

cv2.imshow('im2 text', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()