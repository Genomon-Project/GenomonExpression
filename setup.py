#!/usr/bin/env python

from distutils.core import setup

setup(name='genomon_expression',
      version='0.3.0rc1',
      description='Python tools for calculating fkpm values from rna-seq',
      author='Yuichi Shiraishi',
      author_email='friend1ws@gamil.com',
      url='https://github.com/Genomon-Project/GenomonExpression.git',
      package_dir = {'': 'lib'},
      packages=['genomon_expression'],
      scripts=['genomon_expression'],
      license='GPL-3'
     )

