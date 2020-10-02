import cProfile
import cv2
import numpy as np
from cpython cimport array
import array


def cython_color2gray(unsigned char[:, :, :]image_name):
    """
    args: A 3-dimensional array, provided by the user as an image, and read with imread.
    Also providing a variable to the array. In that
    way it will not have to find out the variable on every iteration in the for-loop. Making it alot faster
    compared to the python implementation.

    Return: Returns the gray-scale version of the image, as an 3-d array.

    """

    cdef int h, w, c, pikselverdi

    cdef double c1, c2, c3
    c1 = 0.21
    c2 = 0.72
    c3 = 0.07

    for i in image_name:
        for pixels in i:
            pikselverdi = (pixels[0] * c1) + \
                (pixels[1] * c2) + (pixels[2] * c3)
            pixels[0] = pikselverdi
            pixels[1] = pikselverdi
            pixels[2] = pikselverdi

    h, w, c = np.float32(image_name).shape
    print(h, w, c)
    # cv2.imwrite('image.jpg', np.float32(image_name))
    return np.float32(image_name)
