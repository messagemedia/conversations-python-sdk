from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='messagemedia_conversations_sdk',
    version='1.0.0',
    description='The Conversations API allows users to communicate by sending and receiving messages via OTT messaging services',
    long_description=long_description,
    author='MessageMedia Developers',
    author_email='support@apimatic.io',
    url='https://developers.messagemedia.com',
    download_url='https://github.com/messagemedia/messages-python-sdk',
    license='Apache-2.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)
