Installation

1. Download the zip file containing the project

2. cd to the folder

3. run "pip install -e ."

On success the terminal will show:

Obtaining file:///Users/edvardunsvag/Downloads/grayAndSepiaConvertion-master
Installing collected packages: Grey
Attempting uninstall: Grey
Found existing installation: Grey 1.0
Uninstalling Grey-1.0:
Successfully uninstalled Grey-1.0
Running setup.py develop for Grey
Successfully installed Grey

Running the functions

4. You can then run "run_instapy"
   Example: run_instapy -g -f 'rain.jpg' -o 'image.jpg' -i numpy

For help, run : "run_instapy -h"
Running that command will give you the following display in the terminal:

This is the interface description

optional arguments:
-h, --help helpful message showing flags and usage of instapy
-f FILE, --file FILE The file you wish to apply effect to
-se, --sepia Select sepia filter
-g, --gray Select gray filter
-Sc SCALE, --scale SCALE
Scale factor to resize image
-i {numpy,python,cython,numba}, --implementation {numpy,python,cython,numba}
Choose the implementation
-o OUT, --out OUT The output filename

Running the tests

1.
