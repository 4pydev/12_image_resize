import os.path
import argparse
from PIL import Image


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Path to initial image file")
    parser.add_argument("-w", "--width",
                        type=int,
                        help="Width of resized image")
    parser.add_argument("-ht", "--height",
                        type=int,
                        help="Height of resized image")
    parser.add_argument("-s", "--scale",
                        type=float,
                        help="Scale of resizing image")
    parser.add_argument("-p", "--new_path",
                        help="The path to directory you want"
                             " to save resized image")
    return parser


def load_img(path_to_original_img):
    return Image.open(path_to_original_img)


def is_not_correct_params(params):
    new_width, new_height, scale = params
    return scale and (new_width or new_height)


def get_new_img_size(initial_img_size, params):
    initial_width, initial_height = initial_img_size
    new_width, new_height, scale = params
    if scale:
        return round(scale * initial_width), round(scale * initial_height)
    elif not scale:
        if not new_height:
            return new_width, round(
                new_width / initial_width * initial_height)
        elif not new_width:
            return round(new_height / initial_height *
                         initial_width), new_height
        else:
            return new_width, new_height


def get_new_img_full_path(path_to_original_img,
                          new_size,
                          path_to_new_img=None):
    if not path_to_new_img:
        path_to_new_img = os.path.dirname(
            os.path.abspath(path_to_original_img))
    width, height = new_size
    size_string = "_{}x{}".format(width, height)
    new_img_basename = size_string.join(
        os.path.splitext(os.path.basename(path_to_original_img)))

    return "{}/{}".format(path_to_new_img, new_img_basename)


def create_new_image_file(initial_img,
                          new_size,
                          new_img_full_path):
    initial_img.resize(new_size).save(new_img_full_path)


def get_proportions_warning(initial_img, new_size):
    initial_width, initial_height = initial_img.size
    new_width, new_height = new_size
    if round(initial_width/initial_height, 1) != round(
                    new_width/new_height, 1):
        print("Warning: Origin image's proportions will change!")


if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()

    params = (
        args.width,
        args.height,
        args.scale
    )
    path_to_original_img = args.path
    path_to_new_img = args.new_path

    initial_img = load_img(path_to_original_img)
    initial_img_size = initial_img.size

    if is_not_correct_params(params):
        parser.error("Wrong parameters! "
                     "There aren't a width (or/and a height) and"
                     " a scale at the same time.")
    new_img_size = get_new_img_size(initial_img_size, params)

    new_img_full_path = get_new_img_full_path(
        path_to_original_img,
        new_img_size,
        path_to_new_img
    )

    get_proportions_warning(initial_img,
                            new_img_size)
    create_new_image_file(initial_img,
                          new_img_size,
                          new_img_full_path)
