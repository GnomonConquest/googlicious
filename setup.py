from setuptools import setup

setup(
    name='googlicious',
    version='0.1',
    author='Dimitry Dukhovny',
    author_email='dimitry@securitystandard.net',
    maintainer='Dimitry Dukhovny',
    maintainer_email='dimitry@securitystandard.net',
    packages=['googlicious', 'googlicious.test'],
    url='',
    license='LICENSE',
    description='Label Gdrive content with rules.',
    long_description=open('README.rst').read(),
    install_requires=[
        "google-api-python-client >= 1.2",
        "oauth2client >= 4.0.0",
        "PyYAML >= 3.0",
        "pydrive"
    ],
)