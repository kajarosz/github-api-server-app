from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='githubapp',
    version='1.0.0',
    description='Simple Flask REST API utilizing Github API to serve any users repos.',
    author='Karolina Jarosz',
    author_email='karolinaannajarosz@gmail.com',
    url='https://github.com/kajarosz/github-api-server-app',
    install_requires=required,
    packages=find_packages(),
)