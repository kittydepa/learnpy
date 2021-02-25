try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47 yo',
    'author': 'Kitterine Depa',
    'url': 'Dont have one yet.',
    'download_url': 'Where to get it.',
    'author_email': 'kitty@kittysci.se',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)