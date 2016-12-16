#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 personal-IO
#

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="personal-IO",
    packages=['personal-IO'],
    version="0.1",
    zip_safe=False,
    long_description=README,
    include_package_data=True,
    license='MIT',
    description="Sistema para la administracion de entrada y salidas de personal",
    url='https://github.com/hostelix/personal-IO/',
    author="Israel Lugo",
    author_email="hostelixisrael@gmail.com",
)