import codecs
import os.path

from setuptools import setup, find_packages

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return codecs.open(fpath(fname), encoding='utf-8').read()

HB_CONFIG_VERSION = '0.4.0'

setup (
    name='hb-config',
    version=HB_CONFIG_VERSION,
    author='Dongjun Lee',
    url='https://github.com/DongjunLee/hb-config',
    author_email='humanbrain.djlee@gmail.com',
    description='easy to configure your python packge',
    ong_description=read(fpath('README.md')),
    keywords = ['config', 'util'],
    license='MIT license',
    packages=find_packages(),
    install_requires=[
        'pyyaml'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
