from setuptools import setup
from setuptools import find_packages

setup(
    name='botx_mask_rcnn',
    version='0.0.1',
    description='packaged mask rcnn for botx project usage',
    author_email='tyan_chiau@berkeley.edu',
    url='https://superbotx.github.io/packaged_mask_rcnn/',
    classifiers=[
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Topic :: Software Development :: Libraries',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(exclude=['example_*'])
)
