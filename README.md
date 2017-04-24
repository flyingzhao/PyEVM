# Python implementation of EVM(Eulerian Video Magnification)

This is a python implementation of eulerian video magnification《[Eulerian Video Magnification for Revealing Subtle Changes in the World](http://people.csail.mit.edu/mrub/evm/)》.
>Our goal is to reveal temporal variations in videos that are difficult or impossible to see with the naked eye and display them in an indicative manner. Our method, which we call Eulerian Video Magnification, takes a standard video sequence as input, and applies spatial decomposition, followed by temporal filtering to the frames. The resulting signal is then amplified to reveal hidden information.Using our method, we are able to visualize the flow of blood as it fills the face and also to amplify and reveal small motions. Our technique can run in real time to show phenomena occurring at temporal frequencies selected by the user.

## Install OpenCV3
Since the OpenCV3.X does not support Python3, you need to install opencv3 manually.

Firstly,download opencv3 for python3:
>OpenCV3 for Python3: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

Then install opencv3 with pip:
```
pip install opencv_python-3.1.0-cp35-cp35m-win_amd64.whl
```

## Other Libraries
* SciPy for signal processing
* NumPy for image processing

## Result
Original video：
![原图](http://img.blog.csdn.net/20160927155312178)

Color magnification：
![色彩放大](http://img.blog.csdn.net/20160927155358125)
The color of chest changes.

Motion magnification：
![运动放大](http://img.blog.csdn.net/20160927155455071)
You can see the motion of chest has been magnified.

## Chinese version
You can read my blog for more information
>http://blog.csdn.net/tinyzhao/article/details/52681250
