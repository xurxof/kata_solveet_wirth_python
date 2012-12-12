try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Wirth subsecuences',
    'author': 'Xurxo Fresco Barbeito',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'xurxof@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['wirth'],
    'scripts': [],
    'name': 'wirth'
}

setup(**config)
