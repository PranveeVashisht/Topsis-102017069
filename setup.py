from distutils.core import setup
def readme():
    with open("README.md") as f:
        README = f.read()
    return README
setup(
  name = 'Topsis-102017069',         
  packages = ['Topsis-102017069'],  
  version = '0.4',     
  license='MIT',       
  description = 'TOPSIS Package for Multiple Criteria Decision Making', 
  long_description=readme(),
  long_description_content_type="text/markdown",
  author = 'PRANVEE VASHISHT',                   
  author_email = 'pranveevashisht@gmail.com',    
  url = 'https://github.com/PranveeVashisht/Topsis-102017069',   
  download_url = 'https://github.com/PranveeVashisht/Topsis-102017069/archive/refs/tags/v_04.tar.gz',    
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
