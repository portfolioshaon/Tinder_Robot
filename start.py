#-*- coding:utf-8 -*-
# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
#teseract

import pyautogui,cv2,time, os.path
import numpy as np
import matplotlib.pyplot as plt
from random import randint

#Constants
fpat = "../capture_images/tinder_faces/"
fpato = "../capture_images/tinder_others/"

#Functions
def remove_multi_space(text):
    import re
    return re.sub(' +',' ',text)

def common_words(text1, text2):
    text1 = text1.split(" ")
    text2 = text2.split(" ")

    com_list = []
    for w1 in text1:
        for w2 in text2:
            if w1 == w2:
                com_list.append(w1)

    return com_list

def image_to_text(filename):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", required=True,    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
        help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    # load the example image and convert it to grayscale
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ## cv2.imshow("Image", gray)

    # check to see if we should apply thresholding to preprocess the
    # image
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif args["preprocess"] == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)

    # show the output images
    # cv2.imshow("Image", image)
    

    ## cv2.imshow("Output", gray)
    #cv2.waitKey(0)

    return text



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#getting dimension of image frame
print("define diagonal region")
ab = input('position for Left-top corner')
c, d = pyautogui.position()
print("position for Left-top corner",c,d)
ab = input('position for right-bottom corner')
e, f = pyautogui.position()
print("position for right-bottom corner",e,f)
print("Got Frame Co-ordinates left, top, widhth, height =",(c , d , e-c, f-d)) 


    

# When you load an image using OpenCV it loads that image into BGR color space by default. To show the colored image using `matplotlib` we have to convert it to RGB space. Following is a helper function to do exactly that. 

# In[2]:

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# ### Code - Haar Cascade Classifier

# XML training files for Haar cascade are stored in `opencv/data/haarcascades/` folder.
# 
# First we need to load the required XML classifier. Then load our input image in grayscale mode. Many operations in OpenCV **are done in grayscale**.

# In[3]:

#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')


from msvcrt import getch

ab = input('position for like')
#time.sleep(3)
x, y = pyautogui.position()
print("like Cor",x,y)
ab = input('position for dislike')
#time.sleep(3)
a, b = pyautogui.position()
print("dislike Cor",a,b)

print("Going for loop")
while True:
    """
    keypress = ord(getch())
    if keypress == 13:
        break
    """
    
	#load test iamge
    image = pyautogui.screenshot('my_screenshot.png')
    test1 = cv2.imread('my_screenshot.png')
	# 'data/test1.jpg'

	#convert the test image to gray image as opencv face detector expects gray images
    gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

	#display the gray image using OpenCV
	# cv2.imshow('Test Imag', gray_img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	#or if you have matplotlib installed then 
    plt.imshow(gray_img, cmap='gray')


	# Now we find the faces in the image with **`detectMultiScale`**. If faces are found, this function returns the positions of detected faces as Rect(x,y,w,h).

	# In[4]:

	#let's detect multiscale (some images may be closer to camera than others) images
    faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);

	#print the number of faces found
    FLEN = len(faces)
    print('Faces found: ', FLEN)
    
    
    dead_end = False
    text_END = remove_multi_space(image_to_text("my_screenshot.png"))

    for word in ["Payment","subtotal","BDT"]:
        if word in text_END:
            dead_end = True

    
    if(len(faces) > 0):
        pyautogui.click(x,y)
		
        path = fpat+str(random_with_N_digits(5))+"f.png"
        while os.path.exists(path):
            path = ""
            path = fpat+str(random_with_N_digits(5))+"f.png"

        image = pyautogui.screenshot(path,region=(c , d , e-c, f-d))
        path = ""
    elif(dead_end):
        print("Limit ends")
        break        
    elif(len(faces) == 0):
        pyautogui.click(a,b)
		
        path = fpato+str(random_with_N_digits(5))+"o.png"
        while os.path.exists(path):
            path = ""
            path = fpato+str(random_with_N_digits(5))+"o.png"
            
        image = pyautogui.screenshot(path,region=(c , d , e-c, f-d))
        path = ""
    
    #sleep is crucial for image capture
    time.sleep(2)