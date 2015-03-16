#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="django-march-madness",
    version="0.1.0",
    author="Colin Stoner",
    author_email="cstoner@novoconstruction.com",
    packages=[
        "django-march-madness",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["django-march-madness/manage.py"],
)
