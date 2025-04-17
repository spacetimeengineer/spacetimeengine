from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spacetimeengine",
    version="0.1.11",
    packages=find_packages(include=["spacetimeengine", "spacetimeengine.*"]),
    author="Michael.C Ryan",
    author_email="spacetime.engineer@gmail.com",
    description="A Python physics utility which can analyze any given metric solution to the Einstein field equations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spacetimeengineer/spacetimeengine",
    project_urls={
        "Documentation": "https://github.com/spacetimeengineer/spacetimeengine#readme",
        "Source": "https://github.com/spacetimeengineer/spacetimeengine",
        "Tracker": "https://github.com/spacetimeengineer/spacetimeengine/issues",
    },
    license="BSD License",
    install_requires=[
        "sympy>=1.0"
    ],
    extras_require={
        "testing": ["nose"]
    },
    tests_require=[
        "nose"
    ],
    test_suite="nose.collector",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.6",
    include_package_data=True,  # Ensures files specified in MANIFEST.in are included
    zip_safe=False,  # Ensures the package can be safely installed as a directory
)