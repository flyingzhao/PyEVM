import cv2
import numpy as np

def rgb2ntsc(src):
    rows=src.shape[0]
    cols=src.shape[1]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    T = np.array([[0.114, 0.587, 0.298], [-0.321, -0.275, 0.596], [0.311, -0.528, 0.212]])
    for i in range(rows):
        for j in range(cols):
            dst[i, j]=np.dot(T,src[i,j])
    return dst

def ntsc2rbg(src):
    rows=src.shape[0]
    cols=src.shape[1]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    T = np.array([[1, -1.108, 1.705], [1, -0.272, -0.647], [1, 0.956, 0.620]])    #todo:T改成矩阵的逆运算
    for i in range(rows):
        for j in range(cols):
            dst[i, j]=np.dot(T,src[i,j])
    return dst


if __name__=="__main__":

    img=cv2.imread("1.jpg")
    cv2.imshow("hello", img)
    print(img[0,0])
    nst=rgb2ntsc(img)
    cv2.imshow("h",nst)
    print(nst[0,0])
    bgr=ntsc2rbg(nst)
    cv2.imshow("hh", bgr)
    print(bgr[0, 0])

    cv2.waitKey()
