from __future__ import unicode_literals

from datetime import date
from reviewboard.extensions.packaging import setup
from subprocess import check_output

GIT_REV_CMD = "git rev-parse --short HEAD".split()
GIT_TIMESTAMP_CMD = "git show -s --format=%ct HEAD".split()

rev = check_output(GIT_REV_CMD).decode('utf-8').strip()
timestamp = check_output(GIT_TIMESTAMP_CMD).decode('utf-8').strip()

PACKAGE = "rb-autocomplete-contains"
VERSION = "{0:%Y}.{0:%m}.{0:%d}+{1}".format(
    date.fromtimestamp(float(timestamp)), rev)

setup(
    name=PACKAGE,
    version=VERSION,
    description="Review Board extension to enhance review groups autocomplete",
    long_description=open('README.rst').read(),
    author='Erik Johansson',
    author_email='erik@ejohansson.se',
    url='https://github.com/erijo/rb-autocomplete-contains',
    packages=["rb_autocomplete_contains"],
    entry_points={
        'reviewboard.extensions':
        '%s = rb_autocomplete_contains.extension:AutocompleteContains'
        % PACKAGE,
    },
    package_data={
        b'rb_autocomplete_contains': [
            'templates/autocomplete_contains/*.html',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Quality Assurance',
    ],
)