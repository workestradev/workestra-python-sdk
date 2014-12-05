import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "workestra",
    version = "1.0.0",
    author = "Workestra Dev",
    author_email = "info@workestra.co",
    description = ("A Python SDK library for the Workestra Api."),
    license = "MIT",
    keywords = "Python SDK library for the Workestra",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['workestra'],
    install_requires=[
        "requests",
    ],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Productivity",
        "License :: OSI Approved :: MIT License",
    ],
)