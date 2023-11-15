import cv2
import numpy as np


poster=cv2.imread("odevfoto1.jpg",0)  # fotoğrafı alma
cv2.imshow("odevfoto1",poster)  # fotoğrafı gösterme
cv2.waitKey()  # fotoğrafı ekrana belli bir süre gösterme

hist= np.zeros(256)
[h,w]=np.shape(poster)

for i in range (0,h):    # pikesllere göre histogram değerleri atma
    for j in range (0,w):
        k=poster[i,j]
        hist[k]=hist[k]+1

for l in range (0,256): # histogram dizisi bastırma
    print(l,"<=>",hist[l])