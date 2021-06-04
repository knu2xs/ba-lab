from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='ba_lab',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Potentially useful and completely unsupported ideas.',
    long_description=long_description,
    author='Esri ArcGIS Business Analyst Development Team',
    license='Apache 2.0',
)
