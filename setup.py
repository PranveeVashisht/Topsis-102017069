from distutils.core import setup
from pathlib import Path
setup(
  name = 'Topsis-102017069',         # How you named your package folder (MyLib)
  packages = ['Topsis-102017069'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TOPSIS Package for Multiple Criteria Decision Making',   # Give a short description about your library
  author = 'PRANVEE VASHISHT',                   # Type in your name
  url = 'https://github.com/PranveeVashisht/Topsis-102017069',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/PranveeVashisht/Topsis-102017069/archive/refs/tags/v_111.tar.gz',    # I explain this later on
  keywords = ['Topsis', 'MCDM', 'package'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  # read the contents of your README file

  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ]
)
