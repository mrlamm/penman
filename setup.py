#!/usr/bin/env python3

import os

from setuptools import setup

base_dir = os.path.dirname(__file__)

long_description = ''
with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# thanks: https://snarky.ca/clarifying-pep-518/
docs_require = [
    'sphinx',
    'sphinx-rtd-theme',
    'sphinx_autodoc_typehints'
]
tests_require = [
    'pytest'
]


setup(
    name='Penman',
    version='0.7.0-beta',
    description='PENMAN notation for graphs (e.g. AMR).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/goodmami/penman',
    author='Michael Wayne Goodman',
    author_email='goodman.m.w@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities'
    ],
    keywords='nlp semantics amr',
    py_modules=['penman'],
    install_requires=[
    ],
    extras_require={
        'docs': docs_require,
        'tests': tests_require,
        'dev': docs_require + tests_require,
    }
    # entry_points={
    #     'console_scripts': [
    #         'penman=...'
    #     ]
    # }
)
