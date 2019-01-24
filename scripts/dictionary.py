# -*- coding: utf-8 -*-
import click
import csv
import json

from lisa.models.bank_branch import BankBranch
from lisa.models.occupation import Occupation
from lisa.models.zip import Zip

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

@dictionary.command(name='create_occupations')
@click.argument('input', type=click.Path(exists=True))
def create_occupations(input):
  '''
    Create occupations from CSV file
  '''
  with open(input, mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader( csv_file, delimiter=';')
    Occupation.drop_collection()
    
    header= [
      'post',
      'code',
      'postNickName1',
      'postNickName2',
      'postNickName3',
      'postNickName4',
      'postNickName5',
      'postNickName6',
      'postNickName7'
    ]
    
    for each in reader:
        row={}
        print("{}".format(each['post']))
        for field in header:
            row[field]=each[field]

        try:
          occupation = Occupation(**row)
          occupation.save()
        except Exception as e:
          print(e)

@dictionary.command(name='create_zips')
@click.argument('input', type=click.Path(exists=True))
def create_zips(input):
  '''
    Create zips from CSV file
  '''
  with open(input, mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader( csv_file, delimiter=';')
    Zip.drop_collection()
    
    header= [
      'city',
      'zip',
      'downtownDistance',
      'minimalBorderDistance',
      'minimalSlumDistance',
      'nextBorderCountry',
      'nextBorderState',
      'nextBorderTown',
      'outskirtsReference',
      'populationalRank',
      'primeLocationBranchesNumber',
      'primeLocationBranchesRecency',
      'regularBranchesNumber',
      'regularBranchesRecency',
      'state',
      'townCharacteristics',
      'VIPBranchesNumber',
      'VIPBranchesRecency',
      'zipAddressIsSlum',
      'longitude',
      'latitude',
      'region',
      'population',
      'cityNickName1',
      'cityNickName2',
      'cityNickName3',
      'cityNickName4',
      'cityNickName5',
      'cityNickName6',
      'cityNickName7',
      'cityNickName8',
      'cityNickName9',
      'cityNickName10'
    ]
    
    for each in reader:
        row={}
        print("{}".format(each['zip']))
        for field in header:
            row[field]=each[field]

        try:
          zip = Zip(**row)
          zip.save()
        except Exception as e:
          print(e)