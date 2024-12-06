import os
import sys
from numpy.distutils.core import Extension, setup
from distutils import sysconfig

_version = '0.2.4'

# Ensure dependencies are installed
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

# Set up the correct path
source_dir = os.path.join(os.getcwd(), 'src', 'pyhspf')  # This is the directory where your source code is located

# Ensure the correct directory and files are used
files = [os.path.join(source_dir, 'hspf13', f) for f in os.listdir(os.path.join(source_dir, 'hspf13'))
         if f.endswith('.c') or f.endswith('.f')]  # Look for .c and .f files

fflags = ['-O3', '-fno-automatic', '-fno-align-commons']
requires = ['numpy', 'scipy', 'matplotlib']

setup(
    name='pyhspf',
    version=_version,
    description="Python Extensions for utilizing the Hydrological Simulation Program in Fortran (HSPF)",
    author='David Lampert',
    author_email='david.lampert@okstate.edu',
    url='https://github.com/djlampert/PyHSPF',
    license="MIT",
    long_description="PyHSPF is a library for hydrological simulations using the Hydrological Simulation Program in Fortran (HSPF).",
    keywords=['hydrology', 'watershed modeling', 'GIS'],
    platforms=['Windows', 'Linux'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
    ],
    packages=['pyhspf', 'pyhspf.core', 'pyhspf.preprocessing', 'pyhspf.calibration', 'pyhspf.forecasting'],
    package_dir={'pyhspf': 'src/pyhspf', 'core': 'src/pyhspf/core', 'preprocessing': 'src/pyhspf/preprocessing',
                 'calibration': 'src/pyhspf/calibration', 'forecasting': 'src/pyhspf/forecasting'},
    package_data={'pyhspf': ['HSPF13.zip'], 'pyhspf.core': ['hspfmsg.wdm', 'attributes']},
    data_files=[('/usr/local/lib/python3.8/site-packages', ['src/pyhspf/hspfmsg.wdm'])],
    ext_modules=[Extension(name='hspf', sources=files, extra_link_args=[], extra_f77_compile_args=fflags)]
)
