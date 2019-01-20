import os
from mongoengine import *

host = os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else 'http://localhost'
env = os.environ['ENV'] if 'ENV' in os.environ else 'development'

if env == 'development':
  connect(db='lisa')
else:
  connect(
    db='lisa',
    host=host)
