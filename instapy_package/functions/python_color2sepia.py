import cv2
import cProfile
import numpy as np


def python_color2sepia(image_name):
    """
    This function takes a 3-dimensional array, made by imread, and adjust each pixel in every channel with
    the correct values provided from the sepia-matrix. Then it uses the updated 3d-array to write to file (image.jpg).
    A lambda function is included to check for some edgecases. 

    Args: 3-D array
    Returns: returns the sepia version of the image, as an 3-d array. 

    """
    sepiaMatrix = [[0.393, 0.769, 0.189],
                   [0.349, 0.686, 0.168],   [0.272, 0.534, 0.131]]

    img_float32 = np.float32(image_name)
    image = cv2.cvtColor(img_float32, cv2.COLOR_BGR2RGB)
    for i in image:
        for pixels in i:
            newArr = [0, 0, 0]
            for num in range(len(pixels)):
                pixelVerdi = pixels[0] * sepiaMatrix[num][0] + pixels[1] * \
                    sepiaMatrix[num][1] + pixels[2] * sepiaMatrix[num][2]

                if(pixelVerdi >= 255):
                    pixelVerdi = 255
                newArr[num] = pixelVerdi
            for i in range(len(newArr)):
                pixels[i] = newArr[i]

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    h, w, c = image.shape
    print(h, w, c)
    # cv2.imwrite('image.jpg', image)
    return image


if __name__ == '__main__':
    """
    This code will only be executed if the script is called. It is provided 
    such that it will not be called on import.

    First an image is read and stored as a 3-d array in image.
    Then the function python_color2sepia is run with cProfile for timing purposes.

    """
    image = cv2.imread('rain.jpg')
    cProfile.run('python_color2sepia(image)')
