#
#   file:       tindergarten.py
#
#   purpose:    a simple tinder swipe bot with face detection
#
#   usage:      start this, then start tinder in your browser, adjust window size
#               set all preferences in tinder like age, sex, location
#               as soon as the dismiss buttion appears, picture is analyzed with OpenCV
#               if a face is detected, this profile will be liked
#               drinks, cars, sunsets, flowers and similar are dismissed
#
#   hint:       maybe the samples for the buttons need to be replaced by your own!
#


import cv2
import time
import pyautogui
import tempfile


#
# main
#
imagePath=tempfile.gettempdir()+r"\my_screenshot.png"
print("Tempfile:",imagePath)
while True:
    print ("Waiting for buttons....")
    while True:
        pos = pyautogui.locateCenterOnScreen('but_dismiss.png')
        if pos!=None:
            break
        time.sleep(5)
    print ("Face detection...")
    im1 = pyautogui.screenshot(imagePath)
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )
    anzahl=len(faces)
    print("Found",anzahl,"faces!")
    if anzahl>0:
        pos=pyautogui.locateCenterOnScreen('but_like.png')
    pyautogui.moveTo(pos[0],pos[1],3.0)
    pyautogui.click(pos)
    pyautogui.moveRel(100,100,2.0)
