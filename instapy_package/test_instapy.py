import numpy as np
import cv2
from numba import jit
from .grayscale_image import grayscale_image
from .sepia_image import sepia_image
import random


a_3d_array = np.random.randint(255, size=(400, 600, 3))

imageName = 'testImage.jpg'
file = open(imageName, 'w')
cv2.imwrite(imageName, a_3d_array)


def test_gray():
    implementations = ['cython', 'python', 'numpy', 'numba']
    a_3d_array = cv2.imread(imageName)
    for impl in implementations:
        arr = grayscale_image(imageName, implementation=impl)

    assert arr[:, :, 0].all() == arr[:, :, 1].all()
    assert arr[:, :, 1].all() == arr[:, :, 2].all()

    h1, w1, c1 = arr.shape
    h2, w2, c2 = a_3d_array.shape

    # Check if shape is similar before and after grayscale
    assert h1 == h2
    assert w1 == w2
    assert c1 == c2

    # You should also check that a random pixel has the expected value.
    randomHeight = random.randint(0, 399)
    randomWidth = random.randint(0, 599)
    randomChannel = random.randint(0, 2)

    newArray = a_3d_array[randomHeight][randomWidth]
    pikselVerdi = newArray[0] * 0.21 + newArray[1] * 0.72 + newArray[2] * 0.07
    newArray[0] = pikselVerdi
    newArray[1] = pikselVerdi
    newArray[2] = pikselVerdi
    assert newArray.all() == arr[randomHeight][randomWidth].all()

    # The test should verify that the picture is actually gray and not color.
    if arr[:, :, 0].all() == arr[:, :, 1].all() and arr[:, :, 1].all() == arr[:, :, 2].all():
        print("The test verifyes that the picture is actually gray and not color")
        return True

    print("The test does not verify that the picture is actually gray and not color")
    return False


def test_sepia():
    implementations = ['cython', 'python', 'numpy', 'numba']
    a_3d_array = cv2.imread(imageName)
    for impl in implementations:
        arr = sepia_image(imageName, implementation=impl)

    assert arr[:, :, 0].all() == arr[:, :, 1].all()
    assert arr[:, :, 1].all() == arr[:, :, 2].all()

    h1, w1, c1 = arr.shape
    h2, w2, c2 = a_3d_array.shape

    # Check if shape is similar before and after grayscale
    assert h1 == h2
    assert w1 == w2
    assert c1 == c2

    # The test should verify that the picture is actually gray and not color.
    if arr[:, :, 0].all() == arr[:, :, 1].all() and arr[:, :, 1].all() == arr[:, :, 2].all():
        print("The test verifyes that the picture is actually gray and not color")
        return True

    print("The test does not verify that the picture is actually gray and not color")
    return False


# test_sepia()
