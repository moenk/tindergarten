#
#   file:       tindergarten.py
#
#   purpose:    a simple tinder swipe bot with face detection
#
#   usage:      start this, then start tinder in your browser, maximize window
#               set all preference in tinder like age, sex, location
#               as soon as the dismiss buttion appears, picture is analyzed with OpenCV
#               if a face is detected, this profile will be liked
#               drinks, cars, sunsets, flowers and similar are dismissed
#
#   hint:       maybe the samples for the buttons need to be replaced by you own!
#


import cv2
import time
import pyautogui
import tempfile


# some natural mouse moving
def MouseMoveToBresenham(end):
    d=10
    x1, y1 = pyautogui.position()
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2.0)
    ystep = d if y1 < y2 else -d
    y = y1
    points = []
    for x in range(x1, x2 + 1,d):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
    if swapped:
        points.reverse()
    for coord in points:
        pyautogui.moveTo(coord)


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
    MouseMoveToBresenham(pos)
    pyautogui.click(pos)
    MouseMoveToBresenham(pyautogui.size())
