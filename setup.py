import setuptools
from setuptools import setup, find_packages
import unittest

setup(name="spacetimeengine", packages=find_packages())
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacetimeengine",
    version="0.1.0",
    author="Michael.C Ryan",
    author_email="spacetime.engineer@gmail.com",
    description="A Python utility which will analyze any given metric solution to the Einstein field equations.",
    test_suite='nose.collector',
    tests_require=['nose'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spacetimeengineer/spacetime-engine",
    packages=["sympy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
