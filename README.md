# Image Resizer

This script allows to resize initial image in some mode 
depending on command line's arguments. Resized image save 
into specified directory or original file's directory (by 
default).

Command line's keys:  
   - path-to-original-image> - required argument
    - [-w] - width of resized image (integer)
    - [-ht] - height of resized image (integer)
    - [-s] - scale of resizing (float)
    - [-p] - path to directory where you want to save resized file.

If you specify [-w] or [-ht] keys other value will be calculate automatically with initial image's proportions.

If you specify both [-w] and [-ht] keys new image will made with these parameters.

You can use either [-s] key or [-w][-ht] keys, not together.


# How to use
You need installed python 3.5 and pillow 3.3.0.

In order to run the script print in command line:
```bash
$ python image-resize.py <path-to-original-image> [keys with args]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

