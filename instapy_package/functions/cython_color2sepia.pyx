import cv2
import cProfile
import numpy as np


def cython_color2sepia(unsigned char[:, :, :]image_name):
    """
    args: A 3-dimensional array, provided by the user as an image, and read with imread.
    Also providing a variable to the array. In that
    way it will not have to find out the variable on every iteration in the for-loop. Making it alot faster
    compared to the python implementation.

    Return: Returns the gray-scale version of the image, as an 3-d array.

    """

    cdef double sepiaMatrix[3][3]
    sepiaMatrix[0][:] = [0.393, 0.769, 0.189]
    sepiaMatrix[1][:] = [0.349, 0.686, 0.168]
    sepiaMatrix[2][:] = [0.272, 0.534, 0.131]

    img_float32 = np.float32(image_name)
    image = cv2.cvtColor(img_float32, cv2.COLOR_BGR2RGB)

    cdef int h, w, c, pikselverdi, maksVerdi
    maksVerdi = 255
    cdef int newArr[3]

    for i in image:
        for pixels in i:
            newArr = [0, 0, 0]
            for num in range(len(pixels)):
                pixelVerdi = pixels[0] * sepiaMatrix[num][0] + pixels[1] * \
                    sepiaMatrix[num][1] + pixels[2] * sepiaMatrix[num][2]
                if(pixelVerdi >= maksVerdi):
                    pixelVerdi = maksVerdi
                newArr[num] = pixelVerdi
            for i in range(len(newArr)):
                pixels[i] = newArr[i]

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    h, w, c = image.shape
    print(h, w, c)
    cv2.imwrite('image.jpg', image)
    return image
