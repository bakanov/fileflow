from setuptools import setup, find_packages
from fileflow import __version__

TEST_REQUIRES_PACKAGES = ['moto~=0.4.18', 'coverage~=4.2', 'nose~=1.3.7', 'mock~=1.0.1']

setup(
    name="fileflow",
    version = __version__,
    description="Airflow plugin to transfer arbitrary files between operators.",
    author='Industry Dive',
    author_email='fileflow@industrydive.com',
    url='https://github.com/industrydive/fileflow',
    license='Apache License 2.0',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'airflow~=1.7.0',
        'pandas==0.17.0',
        'boto~=2.38.0'
    ],
    test_suite='nose.collector',
    tests_require=TEST_REQUIRES_PACKAGES,
    extras_require={
        'test': TEST_REQUIRES_PACKAGES,
        'flake8': ['pyflakes==1.0.0',
                   'pep8==1.5.7',
                   'mccabe==0.3.1',
                   'flake8==2.5.1',
                   'flake8-debugger==1.4.0',
                   'pep8-naming==0.3.3'],
        'docs': ['sphinx==1.5.1',
                 'sphinx-rtd-theme==0.1.9']
    }
)
