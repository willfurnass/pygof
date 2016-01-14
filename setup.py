from setuptools import setup, find_packages
import os


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygof',
    version='0.1.1',
    packages=find_packages(),

    install_requires=[
        "numpy >= 1.6",
        "scipy >= 0.10"
    ],

    author='Will Furnass',
    author_email='will@thearete.co.uk',
    description='Goodness of fit metrics for comparing two 1D numpy.ndarrays.',
    license='GPL 3.0',
)
