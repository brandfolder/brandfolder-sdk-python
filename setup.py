import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brandfolder",
    version=f'{os.environ["CIRCLE_TAG"][1:]}',
    author="Brandfolder",
    author_email="developers@brandfolder.com",
    description="A simple wrapper for the Brandfolder API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brandfolder/brandfolder-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['requests>=2']
)
