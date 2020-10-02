import cv2
import cProfile


def python_color2gray(image_name):
    """
    This function takes a 3-dimensional array, made by imread, and adjust each pixel in every channel with
    the correct value. Then it uses the updated 3d-array to write to file (image.jpg).
    Also prints the shape of the array to the console.

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
    # Implemented at first, but did not need it in the larger project (instapy.py)
    # cv2.imwrite('image.jpg', image_name)

    return image_name


if __name__ == '__main__':
    """
    This code will only be executed if the script is called. It is provided 
    such that it will not be called on import.

    First an image is read and stored as a 3-d array in image.
    Then the function python_color2gray is run with cProfile for timing purposes.

    """
    image = cv2.imread('rain.jpg')
    cProfile.run('python_color2gray(image)')
