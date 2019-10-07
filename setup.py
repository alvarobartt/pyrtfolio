#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome @ alvarob96 in GitHub
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='investpy-portfolio',
    version='0.1',
    packages=find_packages(),
    url='https://investpy-portfolio.readthedocs.io/',
    download_url='https://github.com/alvarob96/investpy-portfolio/archive/0.1.tar.gz',
    license='GNU General Public License v3 (GPLv3)',
    author='Alvaro Bartolome',
    author_email='alvarob96@usal.es',
    description='investpy-portfolio - an investpy module to create custom stock portfolios',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'Unidecode>=1.1.1',
        'pandas>=0.25.1',
        'lxml>=4.4.1',
        'setuptools>=41.2.0',
        'requests>=2.22.0'
    ],
    data_files=[],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords='investing, investing-api, investpy, financial-data, stocks, portfolio',
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/alvarob96/investpy-portfolio/issues',
        'Source': 'https://github.com/alvarob96/investpy-portfolio',
        'Documentation': 'https://investpy-portfolio.readthedocs.io/'
    },
)
