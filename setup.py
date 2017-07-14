# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='betrobot',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='Betrobot Project',
    long_description=long_description,

    # Author details
    author='ToDo',
    author_email='ToDo',

    # Choose your license
    license='ToDo',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    # What does your project relate to?
    keywords='sport betting',

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'requests[socks]>=2.11.1',
        'lxml>=3.6.4',
        'beautifulsoup4>=4.5.1',
        'dirtyjson>=1.0.7',
        'pymongo>=3.3.0',
        'plyvel>=0.9',
        'numpy>=1.11.2',
        'pandas>=0.19.0',
        'scipy>=0.18.1',
        'bottle>=0.12.10',
        'tqdm>=4.11.2'
    ]
)
