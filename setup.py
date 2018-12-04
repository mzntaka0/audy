# -*- coding: utf-8 -*-
"""
"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
about = {}
# Get meta-data from version.py
with open(os.path.join(here, 'audy', 'version.py')) as f:
    exec(f.read(), about)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('requirements.txt', 'r') as f:
    requirements = list(map(lambda s: s.replace('\n', ''), f.readlines()))


setup(
        name=about['__title__'],
        version=about['__version__'],
        description=['__description__'],
        long_description=readme,
        author=about['__author__'],
        author_email=['__author_email__'],
        url=about['__url__'],
        license=about['__license__'],
        packages=find_packages(),
        install_requires = [package for package in requirements],
        classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Operating System :: OS Independent',
            'Topic :: Software Development',
            'Topic :: Software Development :: Testing',
            ],
        )

