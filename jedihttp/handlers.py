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


import jedi
import logging
import json
from bottle import response, request, Bottle

try:
  from http import client as httplib
except ImportError:
  import httplib


logger = logging.getLogger( __name__ )
app = Bottle( __name__ )


@app.post( '/healthy' )
def healthy():
  logger.debug( 'received /healthy request' )
  return { 'healthy': True }


@app.post( '/ready' )
def ready():
  logger.debug( 'received /ready request' )
  return { 'ready': True }


@app.post( '/completions' )
def completions():
  logger.debug( 'received /completions request' )
  script = _GetJediScript( request.json )
  return {
      'completions': [ {
        'name':        completion.name,
        'description': completion.description,
        'docstring':   completion.docstring(),
        'module_path': completion.module_path,
        'line':        completion.line,
        'column':      completion.column
      } for completion in script.completions() ]
  }


@app.post( '/gotodefinition' )
def gotodefinition():
  logger.debug( 'received /gotodefinition request' )
  script = _GetJediScript( request.json )
  return _FormatGoToDefinitions( script.goto_definitions() )


@app.post( '/gotoassignment' )
def gotoassignments():
  logger.debug( 'received /gotoassignment request' )
  script = _GetJediScript( request.json )
  return _FormatGoToDefinitions( script.goto_assignments() )


def _FormatGoToDefinitions( definitions ):
  return {
      'definitions': [ {
        'module_path':       definition.module_path,
        'line':              definition.line,
        'column':            definition.column,
        'in_builtin_module': definition.in_builtin_module(),
        'is_keyword':        definition.is_keyword,
        'description':       definition.description,
        'docstring':         definition.docstring()
      } for definition in definitions ]
  }


def _GetJediScript( request_data ):
  return jedi.Script( request_data[ 'source' ],
                      request_data[ 'line' ],
                      request_data[ 'col' ],
                      request_data[ 'path' ] )


@app.error( httplib.INTERNAL_SERVER_ERROR )
def ErrorHandler( httperror ):
  response.content_type = 'application/json'
  return json.dumps( {
    'exception': httperror.exception,
    'message': str( httperror.exception ),
    'traceback': httperror.traceback
  }, default = _Serializer )


def _Serializer( obj ):
  try:
    serialized = obj.__dict__.copy()
    serialized[ 'TYPE' ] = type( obj ).__name__
    return serialized
  except AttributeError:
    return str( obj )
