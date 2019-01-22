# -*- coding: utf-8 -*-
import click
import csv
import json

from lisa.models.bank_branch import BankBranch

@click.group()
def dictionary():
  pass

@dictionary.command(name='create_bank_branches')
@click.argument('input', type=click.Path(exists=True))
def create_bank_branches(input):
  '''
    Create bank branches from CSV file
  '''
  with open(input, mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader( csv_file, delimiter=';')
    BankBranch.drop_collection()
    # db=mongo_client.lisa
    # db.segment.drop()
    
    header= [
      'bank', 
      'branch', 
      'type', 
      'bankName', 
      'bankNickName', 
      'branchName', 
      'attendedOrganization', 
      'zip', 
      'longitude', 
      'latitude', 
      'bankCategory', 
      'annexation', 
      'differentiation', 
      'recency', 
      'activity', 
      'unicity', 
      'startDate', 
      'lastStand', 
      'populationalRank', 
      'outskirtsReference', 
      'townCharacteristics', 
      'region', 
      'addressStreet', 
      'addressNumber', 
      'addressComplement', 
      'neighborhood', 
      'city', 
      'state', 
      'SRFGraphy', 
      'branchNickName1', 
      'branchNickName2', 
      'branchNickName3', 
      'branchNickName4', 
      'branchNickName5', 
      'branchNickName6', 
      'branchNickName7', 
      'branchNickName8', 
      'branchNickName9', 
      'branchNickName10']
    
    for each in reader:
        row={}
        print("{} - {}".format(each['bank'], each['branch']))
        for field in header:
            row[field]=each[field]

        try:
          bank_branch = BankBranch(**row)
          bank_branch.save()
        except Exception as e:
          print(e)
