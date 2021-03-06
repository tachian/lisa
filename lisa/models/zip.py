from mongoengine import *


class Zip(Document):

    zip = StringField(max_length=8)
    city = StringField(max_length=50)
    downtownDistance = StringField(max_length=50)
    minimalBorderDistance = StringField(max_length=50)
    minimalSlumDistance = StringField(max_length=50)
    nextBorderCountry = StringField(max_length=50)
    nextBorderState = StringField(max_length=50)
    nextBorderTown = StringField(max_length=50)
    outskirtsReference = StringField(max_length=50)
    populationalRank = StringField(max_length=50)
    primeLocationBranchesNumber = StringField(max_length=50)
    primeLocationBranchesRecency = StringField(max_length=50)
    regularBranchesNumber = StringField(max_length=50)
    regularBranchesRecency = StringField(max_length=50)
    state = StringField(max_length=50)
    townCharacteristics = StringField(max_length=50)
    VIPBranchesNumber = StringField(max_length=50)
    VIPBranchesRecency = StringField(max_length=50)
    zipAddressIsSlum = StringField(max_length=50)
    longitude = StringField(max_length=50)
    latitude = StringField(max_length=50)
    region = StringField(max_length=50)
    population = StringField(max_length=50)
    cityNickName1 = StringField(max_length=50)
    cityNickName2 = StringField(max_length=50)
    cityNickName3 = StringField(max_length=50)
    cityNickName4 = StringField(max_length=50)
    cityNickName5 = StringField(max_length=50)
    cityNickName6 = StringField(max_length=50)
    cityNickName7 = StringField(max_length=50)
    cityNickName8 = StringField(max_length=50)
    cityNickName9 = StringField(max_length=50)
    cityNickName10 = StringField(max_length=50)


