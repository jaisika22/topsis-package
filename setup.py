import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="topsis-jaisika-102103378",
    version="1.0.0",
    description="topsis package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jaisika22/topsis-package",
    author="Jaisika Bhatia",
    author_email="jaisikabhatia22@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=[],
    
)