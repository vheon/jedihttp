#     Copyright 2017 SUSE Inc. <cbosdonnat@suse.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#    limitations under the License.
import os
from setuptools import setup

setup(
    name = "jedihttp",
    version = "0.0.0",
    author = "Andrea Cedraro",
    author_email = "a.cedraro@gmail.com",
    description = ("HTTP/JSON wrapper around jedi"),
    license = "Apache-2.0",
    url = "https://github.com/vheon/JediHTTP",
    packages = ['jedihttp'],
    scripts = ['jedihttp-server'],
    install_requires = ['waitress',
                        'bottle',
                        'argparse'],
)
