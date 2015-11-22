try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# this grabs the requirements from requirements.txt
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

config = {
    'description': 'Final Year Project',
    'author': 'Niall McShane',
    'author_email': 'niallmcs@hotmail.co.uk',
    'version': '0.1',
    'setup_requires': ["numpy"],
    'install_requires': ['nose', 'matplotlib', 'numpy', 'python-dateutil', 'pytz', 'pyparsing', 'Cycler', 'scipy', 'sympy', 'ipython', 'pandas'],
    'packages': ['brain_project'],
    'scripts': [],
    'name': 'brain_project'
}

setup(**config)

""" Useful link
 http://python-packaging.readthedocs.org/en/latest/dependencies.html

 http://www.ewencp.org/blog/a-brief-introduction-to-packaging-python/
 """