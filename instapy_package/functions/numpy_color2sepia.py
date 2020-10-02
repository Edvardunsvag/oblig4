import cv2
import cProfile
import numpy as np


def numpy_color2sepia(image_name):
    """
    This function takes a 3-dimensional array, made by imread, and adjust each pixel in every channel with
    the correct values provided from the sepia-matrix, Using numpy.
    A lambda function is included to check for some edgecases. 
    Then it uses the updated 3d-array to write to file (image.jpg).

    Args: 3-D array
    Returns: returns the sepia version of the image, as an 3-d array. 

    """
    sepiaMatrix = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168],
                   [0.272, 0.534, 0.131]]

    image = image_name
    red = image[:, :, 0] * sepiaMatrix[0][0] + image[:, :, 1] * \
        sepiaMatrix[0][1] + image[:, :, 2] * sepiaMatrix[0][2]

    green = image[:, :, 0] * sepiaMatrix[1][0] + image[:, :, 1] * \
        sepiaMatrix[1][1] + image[:, :, 2] * sepiaMatrix[1][2]

    blue = image[:, :, 0] * sepiaMatrix[2][0] + image[:, :, 1] * \
        sepiaMatrix[2][1] + image[:, :, 2] * sepiaMatrix[2][2]

    image = np.repeat(blue[:, :, np.newaxis], 3, 2)
    image[:, :, 1] = green[:, :]
    image[:, :, 2] = red[:, :]

    def bigLambda(x): return x if x < 255 else 255
    bigLambda = np.vectorize(bigLambda)
    image = bigLambda(image)

    h, w, c = image.shape
    print(h, w, c)

    # cv2.imwrite('image.jpg', image)
    return image


if __name__ == '__main__':
    """
    This code will only be executed if the script is called. It is provided 
    such that it will not be called on import.

    First an image is read and stored as a 3-d array in image.
    Then the function numpy_color2sepia is run with cProfile for timing purposes.

    """
    image = cv2.imread('rain.jpg')
    cProfile.run('numpy_color2sepia(image)')
