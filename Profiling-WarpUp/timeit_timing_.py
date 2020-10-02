import matplotlib.pyplot as plt
import numpy as np
import timeit


def random_array(size, dim=3):
    """
    Generate a random array of size size and dimension dim
    """
    return np.random.rand(int(size), dim)


def loop(array):
    """
    Takes a numpy array and isolates all points that are within [0.52,0.6]
    for the first column and between [0.88,0.96] for the second column by
    looping through every point.
    """
    filtered_list = []
    for i in range(len(array)):
        # Check if the point is within the rectangle
        if ((array[i][0] >= 0.52)
            and (array[i][1] >= 0.88)
            and (array[i][0] <= 0.6)
                and (array[i][1] <= 0.96)):
            filtered_list.append(array[i])
    return np.array(filtered_list)


def snake_loop(array):
    """
    Takes a numpy array and isolates all points in a given
    range via array indexing by
    looping through every point.
    """
    filtered_list = []
    for i in range(len(array)):
        # Check if the point is within the rectangle
        if (((array[i][0] >= 0.16)
             and (array[i][1] >= 0.16)
             and (array[i][0] <= 0.24)
             and (array[i][1] <= 0.24))
            # 2nd square
            or
            ((array[i][0] >= 0.28)
             and (array[i][1] >= 0.16)
             and (array[i][0] <= 0.36)
             and (array[i][1] <= 0.24))
            # 3nd square
            or ((array[i][0] >= 0.4)
                and (array[i][1] >= 0.16)
                and (array[i][0] <= 0.48)
                and (array[i][1] <= 0.24))
            # 4th square
            or ((array[i][0] >= 0.4)
                and (array[i][1] >= 0.28)
                and (array[i][0] <= 0.48)
                and (array[i][1] <= 0.36))
            # 5th square
            or ((array[i][0] >= 0.52)
                and (array[i][1] >= 0.28)
                and (array[i][0] <= 0.6)
                and (array[i][1] <= 0.36))
            # 5th square
            or ((array[i][0] >= 0.52)
                and (array[i][1] >= 0.4)
                and (array[i][0] <= 0.6)
                and (array[i][1] <= 0.48))
            # 6th square
            or ((array[i][0] >= 0.52)
                and (array[i][1] >= 0.52)
                and (array[i][0] <= 0.6)
                and (array[i][1] <= 0.6))

            # 6th square
            or ((array[i][0] >= 0.52)
                and (array[i][1] >= 0.64)
                and (array[i][0] <= 0.6)
                and (array[i][1] <= 0.72))):
            filtered_list.append(array[i])
    return np.array(filtered_list)


# Generate a random array of size 1e5

array = random_array(1e5)

filtered_array = snake_loop(array)
filtered_array_snack = loop(array)


def random_array_time():

    SETUP_CODE = ''' 
from __main__ import random_array 
from random import randint'''

    TEST_CODE = ''' 
mylist = '100000'
random_array(mylist)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=1,
                          number=1)

    # priniting minimum exec. time

    print('random_array: {}'.format(min(times)))


def snake_loop_time():
    SETUP_CODE = ''' 
from __main__ import snake_loop, random_array
from random import randint'''

    TEST_CODE = ''' 
mylist = random_array(100000)
snake_loop(mylist)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=1,
                          number=1)
    # priniting minimum exec. time
    print('snake_loop: {}'.format(min(times)))


def loop_time():
    SETUP_CODE = ''' 
from __main__ import loop, random_array
from random import randint'''

    TEST_CODE = ''' 
mylist = random_array(100000)
loop(mylist)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=1,
                          number=1)
    # priniting minimum exec. time
    print('snake_loop: {}'.format(min(times)))


random_array_time()
snake_loop_time()
loop_time()


# if running in a jupyter notebook you might this inline
# Measure code execution with inline magic (Jupyter Notebook)
# print('Loop:\t', end='')
# timeit loop(array)

# Plot the results

# if running in a jupyter notebook you might this inline
# matplotlib inline

# plt.figure(figsize=(10, 10))
# plt.title('Plot of Your Filters')
# plt.plot(array[:, 0], array[:, 1], 'k.')
# plt.plot(filtered_array[:, 0], filtered_array[:, 1], 'g.')
# plt.plot(filtered_array_snack[:, 0], filtered_array_snack[:, 1], 'r.')
# plt.show()
