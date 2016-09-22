import cv2
import numpy as np
from matplotlib import pyplot as plt

def rgb2ntsc(src):
    rows=img.shape[0]
    cols=img.shape[1]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    for i in range(rows):
        for j in range(cols):
            B=img[i,j][0]  #B
            G=img[i,j][1]  #G
            R=img[i,j][2]  #R
            T=np.array([[0.114,0.587,0.298],[-0.321,-0.275,0.596],[0.311,-0.528,0.212]])
            [Y,I,Q]=np.dot(T,np.array([[B],[G],[R]]))
            dst[i,j][0]=Y
            dst[i,j][1]=I
            dst[i,j][2]=Q
    return dst

def ntsc2rbg(src):




if __name__=="__main__":

    img=cv2.imread("1.jpg")
    cv2.imshow("hello", img)
    print(img[0,0])
    nst=rgb2ntsc(img[:,:,0])
    cv2.imshow("h",nst)
    print(nst[9,9])
    cv2.waitKey()
