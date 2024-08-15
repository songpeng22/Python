# the_imported.py

# Python 2.7
#import inspect
#imported_by_fname = inspect.currentframe().f_back.f_code.co_filename
#print('{} was imported by {}'.format(__name__, imported_by_fname))

#python 3.1 and newer
"""

from inspect import getframeinfo, getouterframes, currentframe
frame = currentframe()
while frame:
    print(frame.f_code.co_filename)
    frame = frame.f_back
"""

from inspect import getframeinfo, getouterframes, currentframe
frame = currentframe().f_back
while frame.f_code.co_filename.startswith('<frozen'):
    frame = frame.f_back
print(frame.f_code.co_filename)

"""
from traceback import extract_stack
for x in extract_stack():
    if not x[0].startswith('<frozen importlib'):
        print('{} was imported by {}'.format(__name__, x[0]))
        break
"""