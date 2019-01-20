import os
from mongoengine import *

host = os.environ['HOST_MONGO'] if 'HOST_MONGO' in os.environ else 'http://localhost'
port = os.environ['PORT_MONGO'] if 'PORT_MONGO' in os.environ else 27017
username = os.environ['USERNAME_MONGO'] if 'USERNAME_MONGO' in os.environ else None
password = os.environ['PASSWORD_MONGO'] if 'PASSWORD_MONGO' in os.environ else None
env = os.environ['ENV'] if 'ENV' in os.environ else 'development'

if env == 'development':
  connect(db='lisa')
else:
  connect(
    db='lisa', 
    username=username,
    password=password,
    host=host, 
    port=port)