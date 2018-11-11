# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='christmas-tree-sensors',
    version='1.0.0',
    description='Reading a DHT11 and BH1750 sensor on a RPi',
    long_description=readme,
    author='Paul van Assen',
    author_email='source@pvanassen.nl',
    url='https://github.com/pvanassen/christmas-tree-sensors',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)