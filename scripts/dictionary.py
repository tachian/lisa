# -*- coding: utf-8 -*-
import click
import csv
import json

from pymongo import MongoClient

@click.group()
def dictionary():
  pass

@dictionary.command(name='create_bank_agency')
@click.argument('input', type=click.Path(exists=True))
def create_bank_agency(input):
  '''
    CSV to JSON Conversion
  '''
  with open(input, mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader( csv_file, delimiter=';')
    mongo_client=MongoClient()
    db=mongo_client.lisa
    db.segment.drop()
    
    header= ['Bank', 'Branch', 'Type', 'BankName', 'BankNickName', 'BranchName', 'AttendedOrganization', 'ZIP', 'x', 'y', 'BankCategory', 'Annexation', 'Differentiation', 'Recency', 'Activity', 'Unicity', 'StartDate', 'LastStand', 'PopulationalRank', 'OutskirtsReference', 'TownCharacteristics', 'Region', 'AddressStreet', 'AddressNumber', 'AddressComplement', 'Neighborhood', 'City', 'State', 'SRFGraphy', 'BranchNickName1', 'BranchNickName2', 'BranchNickName3', 'BranchNickName4', 'BranchNickName5', 'BranchNickName6', 'BranchNickName7', 'BranchNickName8', 'BranchNickName9', 'BranchNickName10']
    
    for each in reader:
        row={}
        print("{} - {}".format(each['Bank'], each['Branch']))
        for field in header:
            row[field]=each[field]

        db.bank_agency.insert(row)