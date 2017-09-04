#!/usr/bin/env python3

from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='household_microsynth',
  version='0.1',
  description='Household microsynthesis',
  long_description=readme(),
  url='https://github.com/nismod/household_microsynth',
  author='Andrew P Smith',
  author_email='a.p.smith@leeds.ac.uk',
  license='MIT',
  packages=['household_microsynth'],
  zip_safe=False,
  install_requires=['distutils_pytest', 'humanleague', 'ukcensusapi'],
  dependency_links=['git+git://github.com/virgesmith/humanleague.git#egg=humanleague-1.0',
                    'git+git://github.com/virgesmith/UKCensusAPI.git#egg=ukcensusapi'],
  test_suite='nose.collector',
  tests_require=['nose'],
  python_requires='>=3'
  #scripts=['scripts/run_microsynth.py']
)
