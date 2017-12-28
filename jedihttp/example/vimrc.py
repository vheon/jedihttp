import sys
import os

py_folders = [
    'common',
]


def onStartJedihttp():
    work_folder = os.path.realpath(os.path.dirname(__file__))
    for folder in py_folders:
        sys.path.insert(0, os.path.join(work_folder, folder))
