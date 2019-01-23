import unittest

from mongoengine import *
from falcon import testing
from lisa.app import api

class TestCase(unittest.TestCase):

    def setUp(self):
        self.db = connect(db='lisa-test')

    def tearDown(self):
        self.db.drop_database('lisa-test')
        self.db.close()

    def client(self):
        return testing.TestClient(api)
