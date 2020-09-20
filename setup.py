#!/usr/bin/env python3


from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pykostal',
    version='0.0.1',
    author='Andreas Rehn',
    author_email='rehn.andreas86@gmail.com',
    url='https://github.com/DAMEK86/pykostal',
    description='package to communicate with Kostal Piko invertes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['kostal'],
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    install_requires=[
        'async_timeout',
        'aiohttp'
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
            "twine",
            "tox",
        ],
    },
)
