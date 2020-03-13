# Copyright 2019 Alvaro Bartolome @ alvarobartt in GitHub
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements():
    reqs = list()
    with io.open('requirements.txt', encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='pyrtfolio',
    version='0.4',
    packages=find_packages(),
    url='https://pyrtfolio.readthedocs.io/',
    download_url='https://github.com/alvarobartt/pyrtfolio/archive/0.4.tar.gz',
    license='GNU General Public License v3 (GPLv3)',
    author='Alvaro Bartolome',
    author_email='alvarobartt@usal.es',
    description='pyrtfolio - Python package to generate stock portfolios',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(),
    data_files=[],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords='investing, investing-api, investpy, financial-data, stocks, portfolio',
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/alvarobartt/pyrtfolio/issues',
        'Source': 'https://github.com/alvarobartt/pyrtfolio',
        'Documentation': 'https://pyrtfolio.readthedocs.io/'
    },
)
