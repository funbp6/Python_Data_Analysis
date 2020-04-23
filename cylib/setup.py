from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy

setup(
    name="cdepth",
    ext_modules=cythonize("cydepth.pyx", include_path = [numpy.get_include()]),
)