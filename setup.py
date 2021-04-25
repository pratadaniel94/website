import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, here)

requirements_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'requirements.txt')

# with open(requirements_path) as requirements_file:
#     requires = requirements_file.readlines()

setup(
    name='MeuSite',
    version='0.01',
    maintainer='Hamed',
    license='free',
    packages=find_packages(),
    package_data={'': ['*.csv', '*.yml', '*.html']},
    include_package_data=True,
    install_requires='requires',
    long_description=open('README.md').read(),
    zip_safe=False
)
