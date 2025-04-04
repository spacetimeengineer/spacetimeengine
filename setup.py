from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spacetimeengine",
    version="0.1.11",
    packages=find_packages(),
    author="Michael.C Ryan",
    author_email="spacetime.engineer@gmail.com",
    description="A Python physics utility which can analyze any given metric solution to the Einstein field equations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spacetimeengineer/spacetimeengine",
    install_requires=[
        "sympy"
    ],
    tests_require=[
        "nose"
    ],
    test_suite="nose.collector",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.6",
)