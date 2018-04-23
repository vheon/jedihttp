#     Copyright 2015 Cedraro Andrea <a.cedraro@gmail.com>
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


import sys

if sys.version_info[0] >= 3:
    basestring = str
    unicode = str


def encode_string(value):
    return value.encode('utf-8') if isinstance(value, unicode) else value


def decode_string(value):
    return value if isinstance(value, basestring) else value.decode('utf-8')


try:
    dict.iteritems
except AttributeError:
    # Python 3
    def listvalues(dictionary):
        return list(dictionary.values())

    def iteritems(dictionary):
        return iter(dictionary.items())
else:
    # Python 2
    def listvalues(dictionary):
        return dictionary.values()

    def iteritems(dictionary):
        return dictionary.iteritems()
