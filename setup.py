from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = open('README.md').read()

setup(
    name='django-api-sbif',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.2',

    description='API de la Superintendencia de Bancos e Instituciones Financieras de Chile',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/jupitercl/django-api-sbif',

    # Author details
    author='Francisco Jordan',
    author_email='franciscojordan@live.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='django chile api sbif',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[
        'apisbif'
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'django',
        'requests',
        'munch'
    ],
)
