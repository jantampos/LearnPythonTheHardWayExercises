try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 47',
    'author': 'Jan Aubrey T. Tampos',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'janaubrey.tampos@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Exercise 47'
}

setup(**config)