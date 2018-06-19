from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='message_media_conversations',
    version='1.0.0',
    description='The Conversations API allows users to communicate by sending and receiving messages via Over-The-Top (OTT) messaging services. OTT application is an app or service that provides a product over the Internet and bypasses traditional distribution. Here\'s an in-depth explanation of what the term means.This feature is disabled by default. To enable it, you don\'t need to make any changes to your application, just an account configuration change by MessageMedia\'s support team support@messagemedia.com.For our initial release, we\'re releasing Facebook Messenger which allows you to send messages as a Facebook page owner and receive messages from other Facebook users.',
    long_description=long_description,
    author='APIMatic SDK Generator',
    author_email='support@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)