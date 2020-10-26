import os
import sys
from setuptools import find_packages, setup

# This is needed for versioneer to be importable when building with PEP 517.
# See <https://github.com/warner/python-versioneer/issues/193> and links
# therein for more information.
sys.path.append(os.path.dirname(__file__))

import versioneer

setup_kw = {
    "version": versioneer.get_version(),
    "cmdclass": versioneer.get_cmdclass(),
}

setup(
    name='jwodder-auto-test',
    packages=find_packages(),
    author='John T. Wodder II',
    author_email='auto-test@varonathe.org',
    url='https://github.com/jwodder/auto-test',
    **setup_kw,
)
