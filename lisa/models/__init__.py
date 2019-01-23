import os
from mongoengine import *

host = os.environ['MONGODB_URI'] if 'MONGODB_URI' in os.environ else 'http://localhost'
db = os.environ['MONGODB_DB'] if 'MONGODB_DB' in os.environ else 'lisa'
username = os.environ['MONGODB_USER'] if 'MONGODB_USER' in os.environ else ''
password = os.environ['MONGODB_PWD'] if 'MONGODB_PWD' in os.environ else ''
port = os.environ['MONGODB_PORT'] if 'MONGODB_PORT' in os.environ else 27017
env = os.environ['ENV'] if 'ENV' in os.environ else 'development'

if env == 'development':
  connect(db=db)
elif env == 'testing':
  connect(db='lisa-test')
else:
  connect(
      db=db,
      username=username,
      password=password,
      host=host,
      port=63460
  )