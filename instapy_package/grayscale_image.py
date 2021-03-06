import sys
import cv2
import numpy as np

from .functions import *


def grayscale_image(input_filename, output_filename=None, implementation=None, scale=None):
    """
    args: input_filname : an image file, provided by the user
    output_filename : optional output filename, provided by the user
    implementation : a string deciding what kind of implementation the program should run
    scale : optional, a number between 0 - 1, deciding how to scale the image

    Return: Returns the sepia-version  of the image, as an 3-d array.

    """
    # Makes it possible for user to type implementation without quotes.
    implementation = str(implementation)
    image = cv2.imread(input_filename)

    if(scale != None):
        image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    if implementation == 'numpy':
        image = numpy_color2gray(image)
    elif implementation == 'numba':
        image = numba_color2gray(image)
    elif implementation == 'python':
        image = python_color2gray(image)
    elif implementation == 'cython':
        image = cython_color2gray(image)
    else:
        print("You did not type any of the valid implementations: -numpy, -python, -numba")

    if len(sys.argv) > 6:
        cv2.imwrite(output_filename, image)
    return image


# For testing purposes
if __name__ == '__main__':
    if len(sys.argv) == 4:
        grayscale_image(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 2:
        grayscale_image(sys.argv[1])
    else:
        print("Provide an image as an argument")
