import unittest

from mongoengine import *


class TestCase(unittest.TestCase):

    def setUp(self):
        self.db = connect(db='lisa-test')

    def tearDown(self):
        self.db.drop_database('lisa-test')
        self.db.close()
