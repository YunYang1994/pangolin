## About pangolin
[Pangolin](https://github.com/stevenlovegrove/Pangolin) is a lightweight portable rapid development library for managing OpenGL display / interaction and abstracting video input.  For convenience,  I start up a project implements a python binding for 3D visualization library Pangolin. 

## Required dependencies

* OpenGL 
	* (linux) `sudo apt install libgl1-mesa-dev`
* Glew
	* (linux) `sudo apt install libglew-dev`
	* (mac) `sudo port install glew`
* pybind11
	* `sudo python -mpip install numpy pyopengl Pillow pybind11`

## Installation
Pangolin uses the CMake portable pre-build tool. To checkout and build pangolin in the directory 'build', execute the following at a shell (or the equivelent using a GUI):

```bashrc
$ git clone https://github.com/YunYang1994/pangolin.git
$ git submodule init && git submodule update             # for pybind11
$ cd pangolin && mkdir build
$ cd build && cmake ..
$ make -j8
$ cd ..
$ python setup.py install
```