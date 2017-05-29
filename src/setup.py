from setuptools import setup, find_packages

setup (
       name='LogLookup',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['qrz'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='ka1ssr',
       author_email='ka1ssr@gmail.com',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )