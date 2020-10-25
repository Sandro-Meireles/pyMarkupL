# coding=UTF-8
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(

    name='pyMarkupL',


    version='1.0.0b1',
    
    description='Streamline the production of your HTML page using this python framework.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # A página do projeto
    url='https://github.com/Sandro-Meireles/pyMarkupL',

    project_urls = {
        'Source': 'https://github.com/Sandro-Meireles/pyMarkupL'
    },

    # Detalhes do Autor
    author=u'Sandro Meireles',
    author_email='sandro.meirelesdev@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3.6'
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

    ],

    # What does your project relate to?
    keywords='pymarkupl html react css javascript',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', '.gitignore']),

    entry_points = {
        'console_scripts': ['pml=management.pml:main'],
    },
)
