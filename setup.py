#!/usr/bin/env python3
from setuptools import setup



setup(
    name='random-composer',
    version=1.0,

    description="Generate a random composer's name.",
    url='https://github.com/rickh94/random_composer',

    author='Rick Henry',
    author_email='fredericmhenry@gmail.com',

    license='MIT',
    python_requires='>=3.4',
    install_requires=['click',
                      'bs4',
                      'requests'],

    py_modules=['random_composer'],
    entry_points={
        'console_scripts': [
            'random_composer=random_composer:get_composer',
            ],
        },
    )
