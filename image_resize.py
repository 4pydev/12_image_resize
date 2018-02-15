#!/usr/bin/env python3

import os.path
import argparse
from PIL import Image


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        help = "Path to initial image file")
    parser.add_argument('-w', '--width',
                        type=int,
                        help = "Width of resized image")
    parser.add_argument('-ht', '--height',
                        type=int,
                        help = "Height of resized image")
    parser.add_argument('-s', '--scale',
                        type=float,
                        help = "Scale of resizing image")
    parser.add_argument('-p', '--new_path',
                        help = "The path you want to save resized image")
    return parser


def load_img(path_to_original_img):
    return Image.open(path_to_original_img)


def get_new_img_size(initial_img, params):
    initial_width, initial_height = initial_img.size
    new_width, new_height, scale = params
    if scale != None and (new_width == None and new_height == None):
        return round(scale * initial_width), round(scale * initial_height)
    elif scale != None and (new_width != None or new_height != None):
        raise Exception("Wrong parameters! "
                        "There aren't a width (or/and a height) and"
                        " a scale at the same time.")
    elif scale == None:
        if new_height == None:
            return new_width, round(
                new_width / initial_width * initial_height)
        elif new_width == None:
            return round(new_height / initial_height * 
                         initial_width), new_height
        else:
            return new_width, new_height


def get_new_img_full_path(path_to_original_img,
                              new_size, 
                              path_to_new_img=None):
    if path_to_new_img == None:
        path_to_new_img = os.path.dirname(path_to_original_img)
    width, height = new_size
    size_string = "_{}x{}.".format(width, height)
    new_img_basename = size_string.join(
            os.path.basename(path_to_original_img).split('.'))
    return "{}/{}".format(path_to_new_img, new_img_basename)
    

def create_new_image_file(initial_img,
                         new_size, 
                         new_img_full_path):
    initial_img.resize(new_size).save(new_img_full_path)


def get_proportions_warning(initial_img, new_size):
    initial_width, initial_height = initial_img.size
    new_width, new_height = new_size
    if round(initial_width/initial_height, 1) != round(new_width/new_height, 1):
        print("Warning: Origin image's proportions will change!")


if __name__ == '__main__':

    parser = create_parser()
    namespace = parser.parse_args()

    params = (namespace.width, namespace.height, namespace.scale)
    path_to_original_img = namespace.path
    path_to_new_img = namespace.new_path
    
    initial_img = load_img(path_to_original_img)

    new_img_size = get_new_img_size(initial_img, params)
    
    new_img_full_path = get_new_img_full_path(path_to_original_img,
                                                      new_img_size, 
                                                      path_to_new_img)

    get_proportions_warning(initial_img, new_img_size)
    create_new_image_file(initial_img, new_img_size, new_img_full_path)