import setuptools
from setuptools import setup, find_packages
import unittest

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ['sympy']

setuptools.setup(
    name="spacetimeengine",
    version="0.1.11",
    packages=find_packages(),
    author="Michael.C Ryan",
    author_email="spacetime.engineer@gmail.com",
    description="A python physics utility which can analyze any given metric solution to the Einstein field equations.",
    test_suite='nose.collector',
    tests_require=['nose'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spacetimeengineer/spacetimeengine",
    requirements = requirements,
    dependency_links = ['https://pypi.python.org/simple'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ]
)
