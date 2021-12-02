from distutils.core import setup
from setuptools import find_packages
from os.path import basename, splitext
from glob import glob

setup(
    name="advent21",
    version="0.0.1",
    description="The code used to find solutions to problems in Advent of Code 2021",
    author="James Trimarco",
    author_email="james.trimarco@gmail.com",
    install_requires=[],
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
)