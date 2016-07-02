from os import path
import sys

if __package__ is None:
    sys.path.append( path.abspath( path.join( __file__, '..', '..' ) ) )

from jedihttp import main
main.Main()
