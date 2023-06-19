import setuptools
import os
import sys

setuptools.setup(
    name='ytdl',
    version='1.0',
    author='Rigid Lab',
    author_email='phuta@rigidlab.com',
    description='CLI for downloading Youtube videos',
    url='https://github.com/rigidlab/ytdl',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points = {
        'console_scripts':[
            'ytdl=ytdl.main:cli',
         ]
    }
)
