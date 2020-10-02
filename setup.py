from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['instapy_package/functions/cython_color2gray.pyx',
                           'instapy_package/functions/cython_color2sepia.pyx']),
    name='Grey',
    version='1.0',
    entry_points={
        "console_scripts": ["run_instapy=instapy_package.bin.instapy:main"]
    },
    packages=['instapy_package'],
)
