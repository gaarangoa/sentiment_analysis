
#!/usr/bin/python

import sys
import os

BASE_PATH = "/".join(os.getcwd().split('/')[:-1])
sys.path.insert(0, BASE_PATH)
BASE_PATH = "/".join(os.getcwd().split('/'))
sys.path.insert(0, BASE_PATH)


from rest.API import app as application