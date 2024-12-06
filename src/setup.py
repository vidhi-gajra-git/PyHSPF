_version = '0.2.4'

# check for the required and optional dependencies

try:
    import numpy
except:
    print('error: required package "NumPy" is not installed')
    raise

try:
    import scipy
except:
    print('error: required package "SciPy" is not installed')
    raise

try:
    import matplotlib
except:
    print('error: required package "Matplotlib" is not installed')
    raise

try:
    import gdal
except:
    print('warning: preprocessing dependency "GDAL" is not installed')

try:
    import shapefile
except:
    print('warning: preprocessing dependency "PyShp" is not installed')

try:
    import PIL
except:
    print('warning: preprocessing dependency "Pillow" is not installed')

import os, sys, setuptools
from numpy.distutils.core import Extension, setup
from distutils import sysconfig

_directory = '{}/pyhspf'.format(sysconfig.get_python_lib())

_d = """
PyHSPF contains a library of subroutines to run the Hydrological
Simulation Program in Fortran (HSPF), Python extensions to the HSPF
library, and a series of classes for building HSPF input files,
performing simulations, and postprocessing simulation results.
"""

_s = """Python Extensions for utilizing the Hydrological Simulation Program in Fortran (HSPF)"""

_l = """
PyHSPF, Version {}

Copyright (c) 2014, UChicago Argonne, LLC
All rights reserved.
Copyright 2014. UChicago Argonne, LLC. This software was produced under U.S.
Government contract DE-AC02-06CH11357 for Argonne National Laboratory (ANL),
which is operated by UChicago Argonne, LLC for the U.S. Department of Energy.
""".format(_version)

# link flags
if os.name == 'nt': 
    lflags = ['-static']
else:               
    lflags = []

# any additional files that are needed (blank for now)
data_files = []
data_directory = sysconfig.get_python_lib()

# package data
package_data = ['hspfmsg.wdm', 'attributes']

# find all the Fortran and C files
source_dir = 'src/pyhspf'  # Make sure the source directory is correct

files = [os.path.join(source_dir, 'hspf13', f) for f in os.listdir(os.path.join(source_dir, 'hspf13'))
         if f.endswith('.c') or f.endswith('.f')]

# Fortran compilation flags
fflags = ['-O3', '-fno-automatic', '-fno-align-commons']

requires = ['numpy', 'scipy', 'matplotlib']

setup(
    name='pyhspf',
    version=_version,
    description=_s,
    author='David Lampert',
    author_email='david.lampert@okstate.edu',
    url='https://github.com/djlampert/PyHSPF',
    license=_l,
    long_description=_d,
    keywords=['hydrology', 'watershed modeling', 'GIS'],
    platforms=['Windows', 'Linux'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
    ],
    packages=['pyhspf', 'pyhspf.core', 'pyhspf.preprocessing', 'pyhspf.calibration', 'pyhspf.forecasting'],
    package_dir={
        'pyhspf': os.path.join(source_dir, 'pyhspf'),
        'core': os.path.join(source_dir, 'pyhspf', 'core'),
        'preprocessing': os.path.join(source_dir, 'pyhspf', 'preprocessing'),
        'calibration': os.path.join(source_dir, 'pyhspf', 'calibration'),
        'forecasting': os.path.join(source_dir, 'pyhspf', 'forecasting'),
    },
    package_data={'pyhspf': ['HSPF13.zip'], 'pyhspf.core': package_data},
    data_files=[(data_directory, data_files)],
    ext_modules=[Extension(
        name='hspf',
        sources=files,
        extra_link_args=lflags,
        extra_f77_compile_args=fflags
    )]
)
