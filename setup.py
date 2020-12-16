#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#
#   Editor      : VIM
#   File name   : setup.py
#   Author      : YunYang1994
#   Created date: 2020-12-16 20:20:04
#   Description :
#
#================================================================

from setuptools import setup
from setuptools.command.install import install
from distutils.sysconfig import get_python_lib
import glob
import shutil

__version__ = '1.0.0'

__so_file__    = './build/src/pypangolin*.so'
__dylib_file__ = './build/src/libpangolin.dylib'


class CopyLibFile(install):
    """"
    Directly copy library file to python's site-packages directory.
    """

    def run(self):
        install_dir = get_python_lib()
        print(install_dir)
        lib_file = glob.glob(__so_file__)
        dylib_file = glob.glob(__dylib_file__)
        assert len(lib_file) == 1 and len(install_dir) >= 1

        print('copying {} -> {}'.format(lib_file[0], install_dir))
        shutil.copy(lib_file[0], install_dir)

        if len(dylib_file) > 0:
            print('copying {} -> {}'.format(dylib_file[0], install_dir))
            shutil.copy(dylib_file[0], install_dir)



setup(
    name='pangolin',
    version=__version__,
    description='a lightweight portable library for 3D visualization',
    url='https://github.com/YunYang1994/pangolin',
    license='MIT',
    cmdclass=dict(
        install=CopyLibFile
    ),
    keywords='Pangolin, binding, OpenGL, 3D, visualization, Point Cloud',
    long_description="""This is a Python binding for c++ library Pangolin
        (https://github.com/stevenlovegrove/Pangolin).
        Pangolin is a lightweight portable rapid development library for managing
        OpenGL display / interaction and abstracting video input. At its heart is
        a simple OpenGl viewport manager which can help to modularise 3D visualisation
        without adding to its complexity, and offers an advanced but intuitive 3D navigation
        handler. Pangolin also provides a mechanism for manipulating program variables through
        config files and ui integration, and has a flexible real-time plotter for visualising
        graphical data."""
)
