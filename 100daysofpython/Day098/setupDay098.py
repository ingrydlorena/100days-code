from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("Day098.pyx", language_level="3"),
)