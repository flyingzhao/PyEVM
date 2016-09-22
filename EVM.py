import cv2
import numpy as np

#convert RBG to YIQ
def rgb2ntsc(src):
    rows=src.shape[0]
    cols=src.shape[1]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    T = np.array([[0.114, 0.587, 0.298], [-0.321, -0.275, 0.596], [0.311, -0.528, 0.212]])
    for i in range(rows):
        for j in range(cols):
            dst[i, j]=np.dot(T,src[i,j])
    return dst

#convert YIQ to RBG
def ntsc2rbg(src):
    rows=src.shape[0]
    cols=src.shape[1]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    T = np.array([[1, -1.108, 1.705], [1, -0.272, -0.647], [1, 0.956, 0.620]])    #todo:T改成矩阵的逆
    for i in range(rows):
        for j in range(cols):
            dst[i, j]=np.dot(T,src[i,j])
    return dst

#Build Gaussian Pyramid
def buildGaussianPyramid(src,level=3):
    s=src.copy()
    pyramid=[s]
    for i in range(level):
        s=cv2.pyrDown(s)
        pyramid.append(s)
    return pyramid

#Build Laplacian Pyramid
def buildLaplacianPyramid(src,levels=3):
    gaussianPyramid = buildGaussianPyramid(src, levels)
    s=src.copy()
    pyramid=[gaussianPyramid[levels]]
    for i in range(levels,0,-1):
        GE=cv2.pyrUp(gaussianPyramid[i])
        L=cv2.subtract(gaussianPyramid[i-1],GE)
        pyramid.append(L)
    return pyramid

if __name__=="__main__":

    img=cv2.imread("1.jpg")
    cv2.imshow("hello", img)
    # p=buildGaussianPyramid(img)
    p=buildLaplacianPyramid(img)
    cv2.imshow("0",p[0])
    cv2.imshow("1", p[1])
    cv2.imshow("2", p[2])
    cv2.imshow("3", p[3])
    cv2.waitKey()
