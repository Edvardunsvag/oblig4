import cv2
import cProfile
import numpy as np


def numpy_color2gray(image_name):
    """
    This function takes a 3-dimensional array, made by imread, and adjust each pixel in every channel with
    the correct value. This is done using numpy, so that all computationally heavy bits use vector operations.
    Then it uses the updated 3d-array to write to file (image.jpg).
    Prints the shape of the image to the console.

    Args: 3-D array
    Returns: returns the gray-scale version of the image, as an 3-d array.

    """

    image = image_name[:, :, 0] * 0.21 + \
        image_name[:, :, 1] * 0.72 + image_name[:, :, 2] * 0.07
    image = np.repeat(image[:, :, np.newaxis], 3, 2)

    h, w, c = image.shape
    print(h, w, c)
    # cv2.imwrite('image.jpg', image)
    return image


if __name__ == '__main__':
    """
    This code will only be executed if the script is called. It is provided 
    such that it will not be called on import.

    First an image is read and stored as a 3-d array in image.
    Then the function greyScale_Numpy is run with cProfile for timing purposes.

    """
    image = cv2.imread('rain.jpg')
    cProfile.run('numpy_color2gray(image)')
