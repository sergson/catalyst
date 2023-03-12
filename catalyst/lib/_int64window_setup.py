from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize('_int64window.pyx', language_level = "3"),
    include_dirs=[numpy.get_include()])

#python _int64window_setup.py build_ext --inplace