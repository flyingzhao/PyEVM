========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pyevm/badge/?style=flat
    :target: https://readthedocs.org/projects/pyevm
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/vgoehler/PyEVM.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/vgoehler/PyEVM

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/vgoehler/PyEVM?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/vgoehler/PyEVM

.. |requires| image:: https://requires.io/github/vgoehler/PyEVM/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/vgoehler/PyEVM/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/vgoehler/PyEVM/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/vgoehler/PyEVM

.. |codecov| image:: https://codecov.io/gh/vgoehler/PyEVM/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/vgoehler/PyEVM

.. |commits-since| image:: https://img.shields.io/github/commits-since/vgoehler/PyEVM/v0.4.2.svg
    :alt: Commits since latest release
    :target: https://github.com/vgoehler/PyEVM/compare/v0.4.2...master



.. end-badges

Eulerian Video Magnification for Python

This is a python implementation of Eulerian Video Magnification ([Eulerian Video Magnification for Revealing Subtle Changes in the World](http://people.csail.mit.edu/mrub/evm/)).
>Our goal is to reveal temporal variations in videos that are difficult or impossible to see with the naked eye and display them in an indicative manner. Our method, which we call Eulerian Video Magnification, takes a standard video sequence as input, and applies spatial decomposition, followed by temporal filtering to the frames. The resulting signal is then amplified to reveal hidden information.Using our method, we are able to visualize the flow of blood as it fills the face and also to amplify and reveal small motions. Our technique can run in real time to show phenomena occurring at temporal frequencies selected by the user.

This is a fork from [flyingzhao/PyEVM](https://github.com/flyingzhao/PyEVM) as a basis for own work.
It now has an operational command line interface and is install able.



* Free software: BSD 2-Clause License

Installation
============

Up until now it is not available with PyPI, but if it will be you could use this code to install it.

::

    pip install PyEVM

You can install the in-development version with::

    pip install https://github.com/vgoehler/PyEVM/archive/master.zip

needed libraries (that get automatically installed) are:  

- numpy (>=1.17.4)
- opencv-python (>=4.1.2.30)
- scipy (>=1.3.3)


Running
=======

Navigate to sources directory and use

::

   python3 -mpython_eulerian_video_magnification inputfile.video

if you just want to execute the code.

Usage
=====

optional arguments:
  ================================================ ====================================================
  ``-h, --help``                                    show this help message and exit
  ================================================ ====================================================

system arguments:
  ================================================ ====================================================
  ``input``                                          the input video file to work on
  ``-o [O]``                                         output-folder
  ``--color_suffix [COLOR_SUFFIX]``                  the suffix to use for color modified result files
  ``--motion_suffix [MOTION_SUFFIX]``                the suffix to use for motion modified result files
  ``--log {debug,info,warning,error,critical}``      log level
  ================================================ ====================================================

parameters:
  =================================================== ====================================================
  ``-m {color,motion}``                                mode
  ``-c LOW, --low LOW``                                low parameter (creek)
  ``-p HIGH, --high HIGH``                             high parameter (peek)
  ``-l LEVELS, --levels LEVELS``                       levels parameter
  ``-a AMPLIFICATION, --amplification AMPLIFICATION``  amplification parameter
  =================================================== ====================================================

Documentation
=============


https://PyEVM.readthedocs.io/


Development
===========

To run all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
