from mongoengine import *


class BankBranch(Document):

    bank = StringField(max_length=3) 
    branch = StringField(max_length=4) 
    type = StringField(max_length=50) 
    bankName = StringField(max_length=50)
    bankNickName = StringField(max_length=50) 
    branchName = StringField(max_length=100) 
    attendedOrganization = StringField(max_length=100)
    zip = StringField(max_length=50) 
    longitude = StringField(max_length=50) 
    latitude = StringField(max_length=50) 
    bankCategory = StringField(max_length=50)
    annexation = StringField(max_length=50)
    differentiation = StringField(max_length=50)
    recency = StringField(max_length=50)
    activity = StringField(max_length=50)
    unicity = StringField(max_length=50) 
    startDate = StringField(max_length=50)
    lastStand = StringField(max_length=50) 
    populationalRank = StringField(max_length=50)
    outskirtsReference = StringField(max_length=50)
    townCharacteristics = StringField(max_length=50)
    region = StringField(max_length=50)
    addressStreet = StringField(max_length=50)
    addressNumber = StringField(max_length=50)
    addressComplement = StringField(max_length=50)
    neighborhood = StringField(max_length=50)
    city = StringField(max_length=50)
    state = StringField(max_length=50)
    SRFGraphy = StringField(max_length=50)
    branchNickName1 = StringField(max_length=50)
    branchNickName2 = StringField(max_length=50)
    branchNickName3 = StringField(max_length=50)
    branchNickName4 = StringField(max_length=50)
    branchNickName5 = StringField(max_length=50)
    branchNickName6 = StringField(max_length=50)
    branchNickName7 = StringField(max_length=50)
    branchNickName8 = StringField(max_length=50)
    branchNickName9 = StringField(max_length=50)
    branchNickName10 = StringField(max_length=50)