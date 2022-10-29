import cv2
import numpy as np

img=cv2.imread("poster.jpg")
print(img)

rocket=img[120:360,400:500]
img[0:240,500:600]=rocket

display_text="I love coding!"
cv2.putText(img,display_text,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))

cv2.imshow("output",img)
cv2.waitKey(40000)