import sys, re
from util import *

print '<html><head><title>...<title><body>'
for block in blocks(sys.stdin):
    block=re.sub