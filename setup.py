import subprocess
import os
import re
from distutils.core import setup, Command
from distutils.command.sdist import sdist as _sdist

VERSION_PY = """\
# This file is originally generated from Git information by running
#     $ python3 setup.py version
# Distribution tarballs contain a pre-generated copy of this file.

__version__ = '{:s}'
"""

def update_version_py():
    if not os.path.exists('.git'):
        print("This does not appear to be a Git repository.")
        return
    try:
        p = subprocess.Popen([
            "git", "describe", "--tags", "--dirty", "--always"],
            stdout=subprocess.PIPE)
    except EnvironmentError:
        print("unable to run git, leaving ngs/_version.py alone")
        return
    stdout = p.communicate()[0].decode('utf8')
    if p.returncode != 0:
        print("unable to run git, leaving ngs/_version.py alone")
        return
    # we use tags like "python-ecdsa-0.5", so strip the prefix
    ver = stdout.strip()[len('v'):]     # no "v"x.x.x in _version.py
    with open('nextbiopy/_version.py', 'w') as f:
        f.write(VERSION_PY.format(ver))
    print("set nextbiopy/_version.py to '{:s}'".format(ver))

def get_version():
    try:
        f = open("ngs/_version.py")
    except EnvironmentError:
        return None
    for line in f.readlines():
        mo = re.match("__version__ = '([^']+)'", line)
        if mo:
            ver = mo.group(1)
            return ver
    return None


class Version(Command):
    description = "update _version.py from Git repo"
    user_options = []
    boolean_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        update_version_py()
        print("Version is now", get_version())


class sdist(_sdist):
    def run(self):
        # regenerate version number for every release
        update_version_py()
        self.distribution.metadata.version = get_version()
        return _sdist.run(self)


setup(
    name='nextbiopy',
    license='MIT',
    version=get_version(),
    description='Next bio python utility library',
    author=['Liang Bo Wang', 'Wen Wei Liao'],
    author_email=['b98901114@ntu.edu.tw', 'gattacaliao@gmail.com'],
    maintainer=['Liang Bo Wang', 'Wen Wei Liao'],
    maintainer_email=['b98901114@ntu.edu.tw', 'gattacaliao@gmail.com'],
    url='https://github.com/nextbiopy/nextbiopy',
    packages=['nextbiopy'],
    package_data={
        # if any packages contains *.txt or *.rst, include them
        '': ['*.txt', '*.rst'],
    },
    scripts=[],
    long_description=(

    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
    ],
    cmdclass={"version": Version, "sdist": sdist},
)
