'''
Author: Vincent Young
Date: 2022-07-24 04:27:43
LastEditors: Vincent Young
LastEditTime: 2022-10-12 21:00:38
FilePath: /GmailValidChecker/setup.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
from setuptools import setup, find_packages

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name="GmailChecker",
    author="missuo",
    version="0.0.6",
    license='MIT',
    long_description= long_description,
    long_description_content_type="text/markdown",
    author_email="i@yyt.moe",
    description="Gmail validity checker",
    url='https://github.com/missuo/GmailValidChecker',
    packages=find_packages(),
    include_package_data=False,
    platforms='any',
    zip_safe=False,

    install_requires=[
        'requests',
        'selenium'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)