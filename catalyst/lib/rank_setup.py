from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize('rank.pyx', language_level = "3"),
    include_dirs=[numpy.get_include()])

#python rank_setup.py build_ext --inplace