 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

import os
from distutils.core import setup

setup(name='pyRobots -- nao implementation',
      version='0.1',
      license='ISC',
      description='pyRobots-based implementation of Nao APIs',
      author='Séverin Lemaignan',
      author_email='severin.lemaignan@epfl.ch',
      package_dir = {'': 'src'},
      packages=['robots.naoqi', 'robots.naoqi.actions', 'robots.naoqi.poses'],
      scripts=['scripts/nao_test'],
      data_files=[('share/pyrobots', ['share/' + f for f in ['nao_postures.json']]),
                  ('share/doc/pyrobots', ['AUTHORS', 'LICENSE', 'README'])]
      )
