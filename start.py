import pyautogui,cv2,time, os.path
import numpy as np
import matplotlib.pyplot as plt
from random import randint

#Constants
fpat = "../capture_images/tinder_faces/"
fpato = "../capture_images/tinder_others/"

#Functions
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
    
    if(len(faces) > 0):
        pyautogui.click(x,y)
		
        path = fpat+str(random_with_N_digits(5))+"f.png"
        while os.path.exists(path):
            path = ""
            path = fpat+str(random_with_N_digits(5))+"f.png"

        image = pyautogui.screenshot(path,region=(c , d , e-c, f-d))
        path = ""

            
    elif(len(faces) == 0):
        pyautogui.click(a,b)
		
        path = fpato+str(random_with_N_digits(5))+"o.png"
        while os.path.exists(path):
            path = ""
            path = fpato+str(random_with_N_digits(5))+"o.png"
            
        image = pyautogui.screenshot(path,region=(c , d , e-c, f-d))
        path = ""
    time.sleep(2)
