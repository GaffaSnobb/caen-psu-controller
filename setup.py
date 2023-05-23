from setuptools import setup

setup(
    name = 'caen-psu-controller',
    version = '1.0.0.0',    
    description = 'Python interface for Caen Easy Driver',
    # long_description = long_description,
    url = 'https://github.com/GaffaSnobb/caen-psu-controller',
    author = ['Jon Kristian Dahl',],
    author_email = 'jonkd@uio.no',
    packages = ['caen_easy_driver'],
    install_requires = [],

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.11',
    ],
)
