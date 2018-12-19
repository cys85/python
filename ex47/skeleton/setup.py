try:
  from setuptools import setup
except ImportError
  from distutils.core import setup

config = {
  'description': 'My Project',
  'author': 'My Name',
  'url': 'URL ti get it at.',
  'download_url': 'Where to download it.',
  'author_email': 'My email.',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
}

setup(**config)