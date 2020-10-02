import cv2
import numpy as np
from numba import jit
import time


@jit
def numba_color2gray(image_name):
    """
    This function takes a 3-dimensional array, made by imread, and adjust each pixel in every channel with
    the correct value. This type done using numpy and numba. Then it uses the updated 3d-array to write to file (image.jpg).
    The function of numba is explained in the report.

    Args: 3-D array
    Returns: returns the gray-scale version of the image, as an 3-d array.

    """

    for i in image_name:
        for pixels in i:
            pikselverdi = pixels[0] * 0.21 + \
                pixels[1] * 0.72 + pixels[2] * 0.07
            pixels[0] = pikselverdi
            pixels[1] = pikselverdi
            pixels[2] = pikselverdi

    h, w, c = image_name.shape
    print(h, w, c)
    # cv2.imwrite('image.jpg', image_name)
    return image_name


if __name__ == '__main__':
    """
    This code will only be executed if the script is called. It is provided 
    such that it will not be called on import.

    First an image is read and stored as a 3-d array in image.
    Then the function numba_color2gray is run inbetween "start" and "end", using timeit.
    The elapsed time for each compilated is then printed to the terminal.


    """
    # Only needed for time_reporting

    # image = cv2.imread('rain.jpg')

    # start = time.time()
    # numba_color2gray(image)
    # end = time.time()
    # print("Elapsed (with compilation) = %s" % (end - start))

    # # NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
    # start = time.time()
    # numba_color2gray(image)
    # end = time.time()
    # print("Elapsed (after compilation-1) = %s" % (end - start))

    # start = time.time()
    # numba_color2gray(image)
    # end = time.time()
    # print("Elapsed (after compilation-2) = %s" % (end - start))
