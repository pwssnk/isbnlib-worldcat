# -*- coding: utf-8 -*-

"""isbnlib-worldcat -- an isbnlib plugin for the WorldCat service."""


from setuptools import setup


setup(
    name='isbnlib-worldcat',
    version='0.1.0',
    author='pwssnk',
    author_email='',
    url='https://github.com/pwssnk/isbnlib-worldcat',
    download_url='',
    packages=['isbnlib_worldcat/'],
    entry_points = {
        'isbnlib.metadata': ['worldcat=isbnlib_worldcat:query']
    },
    install_requires=["isbnlib>=3.9.1", "pycountry>=1.12.8", "beautifulsoup4>=4.7.1"],
    license='LGPL v3',
    description='An isbnlib plugin for the WorldCat service (https://www.worldcat.org/).',
    keywords='ISBN, isbnlib, WorldCat',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
