import os
from mongoengine import *

host = os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else 'http://localhost'
db = os.environ['MONGODB_DB'] if 'MONGODB_DB' in os.environ else 'lisa'
env = os.environ['ENV'] if 'ENV' in os.environ else 'development'

if env == 'development':
  connect(db=db)
elif env == 'testing':
  connect(db='lisa-test')
else:
  connect(
    db=db,
    host=host
  )
