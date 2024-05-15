import os 
import sys 
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
os.chdir(os.path.join(script_directory, 'SERVER'))
import flask
from config import *
import sys
args = sys.argv