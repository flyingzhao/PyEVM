import cv2
import numpy as np
import scipy.signal as signal
import scipy.fftpack as fftpack


#convert RBG to YIQ
def rgb2ntsc(src):
    [rows,cols]=src.shape[:2]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    T = np.array([[0.114, 0.587, 0.298], [-0.321, -0.275, 0.596], [0.311, -0.528, 0.212]])
    for i in range(rows):
        for j in range(cols):
            dst[i, j]=np.dot(T,src[i,j])
    return dst

#convert YIQ to RBG
def ntsc2rbg(src):
    [rows, cols] = src.shape[:2]
    dst=np.zeros((rows,cols,3),dtype=np.float64)
    T = np.array([[1, -1.108, 1.705], [1, -0.272, -0.647], [1, 0.956, 0.620]])    #todo:T改成矩阵的逆
    for i in range(rows):
        for j in range(cols):
            dst[i, j]=np.dot(T,src[i,j])
    return dst

#Build Gaussian Pyramid
def build_gaussian_pyramid(src,level=3):
    s=src.copy()
    pyramid=[s]
    for i in range(level):
        s=cv2.pyrDown(s)
        pyramid.append(s)
    return pyramid

#Build Laplacian Pyramid
def build_laplacian_pyramid(src,levels=3):
    gaussianPyramid = build_gaussian_pyramid(src, levels)
    s=src.copy()
    pyramid=[gaussianPyramid[levels]]
    for i in range(levels,0,-1):
        GE=cv2.pyrUp(gaussianPyramid[i])
        L=cv2.subtract(gaussianPyramid[i-1],GE)
        pyramid.append(L)
    return pyramid

#load video from file
def load_video(video_filename):
    cap=cv2.VideoCapture(video_filename)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    video_tensor=np.zeros((frame_count,height,width,3),dtype='float')
    x=0
    while cap.isOpened():
        ret,frame=cap.read()
        if ret is True:
            video_tensor[x]=frame
            x+=1
        else:
            break
    return video_tensor,fps

def temporal_ideal_filter(tensor,low,high,fps,axis=0):
    fft=fftpack.fft(tensor,axis=axis)
    frequencies = fftpack.fftfreq(tensor.shape[0], d=1.0 / fps)
    bound_low = (np.abs(frequencies - low)).argmin()
    bound_high = (np.abs(frequencies - high)).argmin()
    fft[:bound_low] = 0
    fft[bound_high:-bound_high] = 0
    fft[-bound_low:] = 0
    iff=fftpack.ifft(fft, axis=axis)
    return np.abs(iff)

def ideal_filter(tensor,low,high,fps,):
    [length,rows,cols,channel]=tensor.shape
    ifft=np.zeros((length,rows,cols,channel))
    for i in range(rows):
       for j in range(cols):
           for k in range(channel):
                f=fftpack.fft(tensor[:,i,j,k])
                frequencies = fftpack.fftfreq(tensor.shape[0], d=1.0 / fps)
                bound_low = (np.abs(frequencies - low)).argmin()
                bound_high = (np.abs(frequencies - high)).argmin()
                f[:bound_low] = 0
                f[bound_high:-bound_high] = 0
                f[-bound_low:] = 0
                iff=fftpack.ifft(f)
                ifft[:,i,j,k]=np.abs(iff)
    return ifft


def gaussian_video(video_tensor,levels=3):
    for i in range(0,video_tensor.shape[0]):
        frame=video_tensor[i]
        pyr=build_gaussian_pyramid(frame,level=levels)
        gaussian_frame=pyr[-1]
        if i==0:
            vid_data=np.zeros((video_tensor.shape[0],gaussian_frame.shape[0],gaussian_frame.shape[1],3))
        vid_data[i]=gaussian_frame
    return vid_data

def amplify_video(gaussian_vid,amplification=50):
    return gaussian_vid*amplification

def reconstract_video(amp_video,origin_video,levels=3):
    final_video=np.zeros(origin_video.shape)
    [height,width]=origin_video[0].shape[0:2]
    for i in range(0,amp_video.shape[0]):
        img = np.ndarray(shape=amp_video[i].shape, dtype='float')
        img[:] = amp_video[i]
        for x in range(levels):
            img=cv2.pyrUp(img)
        img[:height,:width]=img[:height,:width]+origin_video[i]
        final_video[i]=cv2.convertScaleAbs(img[:height,:width])
    return final_video

def save_video(video_tensor):
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    [height,width]=video_tensor[0].shape[0:2]
    writer = cv2.VideoWriter("out.avi", fourcc, 30, (width, height), 1)
    for i in range(0,video_tensor.shape[0]):
        writer.write(cv2.convertScaleAbs(video_tensor[i]))#import bug
    writer.release()

def magnify_color():
    t,f=load_video("baby.mp4")
    gau_video=gaussian_video(t,levels=3)
    print(gau_video[:,1,1,1])
    filtered_tensor=temporal_ideal_filter(gau_video,0.4,3,f)
    print(filtered_tensor[:,1,1,1])
    amplified_video=amplify_video(filtered_tensor)
    print(amplified_video[:,1,1,1])
    final=reconstract_video(amplified_video,t,levels=3)
    print(final[:,1,1,1])
    save_video(final)

if __name__=="__main__":
    magnify_color()

