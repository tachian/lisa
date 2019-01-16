from mongoengine import *


class BankAgencyModel(Document):
    bank_code = StringField(required=True, max_length=3)
    number = StringField(required=True, max_length=4)
    name = StringField(required=True, max_length=16)