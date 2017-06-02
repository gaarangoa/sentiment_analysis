
#!/usr/bin/python

python_home = 'source ~/tensorflow.1.0.1/'

activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import os

BASE_PATH = "/".join(os.getcwd().split('/')[:-1])
sys.path.insert(0, BASE_PATH)
BASE_PATH = "/".join(os.getcwd().split('/'))
sys.path.insert(0, BASE_PATH)



from rest.API import app as application