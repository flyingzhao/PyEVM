# Python implementation of EVM (Eulerian Video Magnification)

This is a python implementation of eulerian video magnification ([Eulerian Video Magnification for Revealing Subtle Changes in the World](http://people.csail.mit.edu/mrub/evm/)).
>Our goal is to reveal temporal variations in videos that are difficult or impossible to see with the naked eye and display them in an indicative manner. Our method, which we call Eulerian Video Magnification, takes a standard video sequence as input, and applies spatial decomposition, followed by temporal filtering to the frames. The resulting signal is then amplified to reveal hidden information.Using our method, we are able to visualize the flow of blood as it fills the face and also to amplify and reveal small motions. Our technique can run in real time to show phenomena occurring at temporal frequencies selected by the user.

This is right a fork from [flyingzhao/PyEVM](https://github.com/flyingzhao/PyEVM) as a basis for own work. Operational objective one is to give it a usable command line interface.

## Install
install requirements:
```
pip install -r requirements.txt
```

needed libraries are:
numpy (1.17.4)
opencv-python (4.1.2.30)
scipy (1.3.3)

see [requirements.txt](requirements.txt)

# modes
Two modes are implemented. A color change and a motion change.
