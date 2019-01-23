from mongoengine import *


class Occupation(Document):

    post = StringField(max_length=100) 
    code = StringField(max_length=3) 
    postNickName1 = StringField(max_length=50)
    postNickName2 = StringField(max_length=50)
    postNickName3 = StringField(max_length=50)
    postNickName4 = StringField(max_length=50)
    postNickName5 = StringField(max_length=50)
    postNickName6 = StringField(max_length=50)
    postNickName7 = StringField(max_length=50)
