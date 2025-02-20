#!/usr/bin/env python3
#############################################################################
# Copyright (c) 2022 Balazs Scheidler <bazsi77@gmail.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# As an additional exemption you are allowed to compile & link against the
# OpenSSL libraries as published by the OpenSSL project. See the file
# COPYING for details.
#
#############################################################################

from setuptools import setup
import platform
import os

install_addons=int(os.getenv('PYMODULES_BUILTINS_ONLY', '0')) == 0

packages_builtin=[
  "syslogng",
  "syslogng.debuggercli",
]
requires_builtin=[]

packages_addons=[
  "syslogng.modules.example",
  "syslogng.modules.kubernetes",
  "syslogng.modules.hypr",
]

requires_addons=[
  # kubernetes
  "kubernetes",
  # hypr
  "requests",
]

python_version = platform.python_version_tuple()
if (int(python_version[0]) == 3 and int(python_version[1]) > 6) or int(python_version[0]) > 3:
  # Compiling type hinted code does not seem to work on <= 3.6.
  # We can remove this condition when the centos-7 support is dropped.
  packages_addons.append("syslogng.modules.s3")
  requires_addons.append("boto3")  # S3

packages = packages_builtin
requires = []
if install_addons:
  packages = packages + packages_addons
  requires = requires + requires_addons

setup(name='syslogng',
      version='1.0',
      description='syslog-ng Python Core & Modules',
      author='Balazs Scheidler',
      author_email='bazsi77@gmail.com',
      url='https://www.syslog-ng.org',
      package_data={"": ["scl/*"]},
      exclude_package_data={"": ["*~"]},
      packages=packages,
      install_requires=requires)
