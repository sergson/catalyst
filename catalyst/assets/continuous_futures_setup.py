from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize('continuous_futures.pyx', language_level = "3"),
    include_dirs=[numpy.get_include()])

#python continuous_futures_setup.py build_ext --inplace