import os 
import sys 
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
os.chdir(script_directory)
import flask
from config import *
import sys
args = sys.argv
from flask import request