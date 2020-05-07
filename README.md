## What does this repository contain?
This repository contains a code for extracting temperature from a thermal image using flir image extractor. 

Please note: This code is valid for only images and the images need to have temperature metadata.

## How to use this repository?
Simply install requirements
	pip install -r requirements.txt
Set your folder paths in main and thats it.

## Why does this not work on videos?
Videos have a collection of a lot of images/frames and hence it cannot contain temperature metadata of each. Even when you try to make a video out of a bunch of thermal images, the exif temperature data will be lost.

## Dependencies
You may need to install exiftool for flir to work.
