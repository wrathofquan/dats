from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [Extension("cython_version", ["cython_version.pyx"])]

setup(
    name='cython version of find_potential_event_ptrs',
    cmdclass={'build_ext':build_ext},
    include_dirs=[numpy.get_include()],
    ext_modules=ext_modules
    )
