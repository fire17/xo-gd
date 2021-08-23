from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '3.2.8'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='xo-gd',
    version=__version__,
    description='Use Python Like You Never Have Before, Easy Acces To: Events and Triggers, Realtime MultiProcessing, Instant Dynamic DB, Filesytem & Web Watchdog, Sockets, MQTT, P2P, API Server, Supports Fast Prototyping To Large Scale Systems',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fire17/xo-gd',
    download_url='https://github.com/fire17/xo-gd/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Tami Bar',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='fire17@gmail.com'
)
