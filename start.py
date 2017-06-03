
#!/usr/bin/python2.7

python_home = '/home/gustavo/tensorflow.1.0.1/'
activate_this = python_home + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/NLP/sentiment/')

from rest.API import app as application

