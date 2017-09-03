from setuptools import setup, find_packages

HB_CONFIG_VERSION = '0.1.0'

setup (
    name='hb-config',
    version=HB_CONFIG_VERSION,
    author='Dongjun Lee',
    packages=find_packages(),
    author_email='humanbrain.djlee@gmail.com',
    description='easy to configure your python packge',
    license='OPEN SOURCE'
)
