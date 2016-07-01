import os.path
import sys

if __package__ is None:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from jedihttp import main
    main.Main()
else:
    from . import main
    main.Main()
