#!/usr/bin/env python3

import os.path
from PIL import Image


def load_img(path_to_original_img):
    return Image.open(path_to_original_img)


def get_new_img_size(initial_img, params):
    initial_width, initial_height = initial_img.size
    new_width, new_height, scale = params
    if scale != None and (new_width == None and new_height == None):
        return round(scale * initial_width), round(scale * initial_height)
    elif scale != None and (new_width != None or new_height != None):
        raise Exception("Wrong parameters!")
    elif scale == None:
        if new_height == None:
            return round(new_width), round(
                    new_width / initial_width * initial_height)
        elif new_width == None:
            return round(new_height / initial_height * 
                         initial_width), round(new_height)
        else:
            return round(new_width), round(new_height)
        
        
def get_resized_img_full_path(path_to_original_img, 
                              new_size, 
                              path_to_resized_img=None):
    if path_to_resized_img == None or path_to_resized_img == "":
        path_to_resized_img = os.path.dirname(path_to_original_img)
    width, height = new_size
    size_string = "_{}x{}.".format(width, height)
    resized_img_basename = size_string.join(
            os.path.basename(path_to_original_img).split('.'))
    print(resized_img_basename)
    return "{}/{}".format(path_to_resized_img, resized_img_basename)
    

def create_resized_image(initial_img, 
                         new_size, 
                         resized_img_full_path):
    initial_img.resize(new_size).save(resized_img_full_path)


def get_proportions_warning(initial_img, new_size):
    initial_width, initial_height = initial_img.size
    new_width, new_height = new_size
    if round(initial_width/initial_height, 1) != round(new_width/new_height, 1):
        print("Warning: Origin image's proportions will change!")


if __name__ == '__main__':
    
    # Initial data
    params = (300, 500, None)
    path_to_original_img = './img/small-kitten.jpg'
    path_to_resized_img = "."
    print(params)
    
    initial_img = load_img(path_to_original_img)

    new_img_size = get_new_img_size(initial_img, params)   
    print("\n")
    
    resized_img_full_path = get_resized_img_full_path(path_to_original_img, 
                                                      new_img_size, 
                                                      path_to_resized_img)
    print(resized_img_full_path)
    get_proportions_warning(initial_img, new_img_size)
    create_resized_image(initial_img, new_img_size, resized_img_full_path)