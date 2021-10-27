import cv2
import random
import time
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("kostka.jpg")

plt.figure()
plt.title("Kostka")
print(type(img))
plt.imshow(img)


img_grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.figure()
plt.title("Sedoton1")
plt.imshow(img_grayscale,cmap="gray")


laplacian = cv2.Laplacian(img_grayscale,cv2.CV_64F)
sobelx = cv2.Sobel(img_grayscale,cv2.CV_64F,1,0,ksize=15)
sobely = cv2.Sobel(img_grayscale,cv2.CV_64F,0,1,ksize=15)

plt.figure()
plt.title("laplacian")
plt.imshow(laplacian,cmap="gray")

plt.figure()
plt.title("sobelx")
plt.imshow(sobelx,cmap="gray")


plt.figure()
plt.title("sobely")
plt.imshow(sobely,cmap="gray")


img_scene= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.title("Scera - barvy fixed")
plt.imshow(img_scene)

img_grayscale2 = cv2.cvtColor(img_scene,cv2.COLOR_RGB2GRAY)
plt.figure()
plt.title("Sedoton2")
plt.imshow(img_grayscale,cmap="gray")


img_gray = img_grayscale -img_grayscale2
plt.figure()
plt.title("ROZDIL")
plt.imshow(img_gray,cmap="gray")


#nacteni pozadi
img_background = cv2.imread("kostka.jpg")
img_grayscale_background = cv2.cvtColor(img_background,cv2.COLOR_RGB2GRAY)
plt.figure()
plt.title("Sedoton pozadi")
plt.imshow(img_grayscale_background,cmap="gray")

#odecteni pozadi
img_subtracted = cv2.subtract(img_grayscale_background,img_grayscale2)
plt.figure()
plt.title("po odecteni pozadi")
plt.imshow(img_subtracted,cmap="gray",vmin=0,vmax=255)


#prahování
_,img_threshol = cv2.threshold(img_subtracted,120,255,cv2.THRESH_BINARY)
plt.figure()
plt.title("prahování")
plt.imshow(img_threshol,cmap="gray",vmin=0,vmax=255)

#eroze
kernel = np.ones((5,5), np.uint8)

image_threshold = cv2.erode(img_threshol, kernel, iterations=2)
plt.figure()
plt.title("eroze")
plt.imshow(image_threshold,cmap="gray",vmin=0,vmax=255)


#dilatace
image_threshold_dil = cv2.dilate(image_threshold,kernel, iterations=8)
plt.figure()
plt.title("dilatace")
plt.imshow(image_threshold_dil,cmap="gray",vmin=0,vmax=255)


#vykreslení výsledku do původního obrázku
contours, hierarchy = cv2.findContours(image_threshold_dil,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
target_contours = []
for contour in contours:
    contour_area = cv2.contourArea(contour)
    if contour_area >300:
        target_contours.append(contour)
cv2.drawContours(img_scene,target_contours, -1,(0,255,0),3)
print(len(target_contours))
plt.figure()
plt.title("nalezene kontury v oprahovanem obrazku (bet pozadí): {}".format(len(target_contours)))
plt.imshow(img_scene)

#nalezení kruhu pomocí Houghovy transformace
circle = cv2.HoughCircles(img_grayscale,cv2.HOUGH_GRADIENT,1,5,param1=50,param2=30,minRadius=10,maxRadius=30)

circles = np.uint16(np.around(circle))
for circle in circles[0,:]:
    #vykreslení kruhu
    cv2.circle(img,(circle[0],circle[1]),circle[2],(0,255,0),8)
    #vykreslení středu kruhu
    cv2.circle(img,(circle[0],circle[1]),2,(0,255,0),3)

plt.figure()
plt.title("nalezene kruhy v obrazku jedné kostky")
plt.imshow(img)

#konvoluce příprava - doostření
kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0],
])

convolved_image = np.zeros((img_grayscale.shape[0] - kernel.shape[0]+1, img_grayscale.shape[1] - kernel.shape[1]+1))
print(img_grayscale.shape)
print(convolved_image.shape)


#konvoluce výpočet
for i in range(convolved_image.shape[0]):
    for j in range(convolved_image.shape[1]):
        patch = img_grayscale[i:i+kernel.shape[0],j:j+kernel.shape[1]]
        result = (patch* kernel).sum()
        convolved_image[i,j] = result

plt.figure()
plt.title("doostreny obrazek")
plt.imshow(convolved_image, cmap="gray")
plt.show()