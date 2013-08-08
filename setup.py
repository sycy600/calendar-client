from setuptools import setup, find_packages

setup(
    name = "event_creator",
    version = "0.1.0",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools', 'oauth2client', 'google-api-python-client', 'python-dateutil'],
)
