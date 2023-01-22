from distutils.core import setup
setup(
  name = 'Topsis-102017069',         
  packages = ['Topsis-102017069'],  
  version = '0.1',      
  license='MIT',      
  description = 'TOPSIS Package for Multiple Criteria Decision Making',   
  author = 'PRANVEE VASHISHT',                  
  author_email = 'pranveevashisht@gmail.com',    
  url = 'https://github.com/PranveeVashisht/Topsis-102017069',   
  download_url = 'https://github.com/PranveeVashisht/Topsis-102017069/archive/refs/tags/v_01.tar.gz',   
  keywords = ['Topsis', 'MCDM', 'package'],  
  install_requires=[         
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
