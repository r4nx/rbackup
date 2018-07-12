#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name='rbackup',
    version='0.0.1a0',
    description='Simple backup script',
    author='Ranx',
    url='https://github.com/r4nx/rbackup',
    py_modules=['rbackup'],
    keywords=['backup'],
    zip_safe=False,
    python_requires='~=3.7',
    install_requires=[
        'click==6.7'
    ],
    extras_require={
        'color': ['colorama==0.3.9']
    },
    entry_points='''
    [console_scripts]
    rbackup=rbackup:main
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Archiving :: Backup'
    ]
)
