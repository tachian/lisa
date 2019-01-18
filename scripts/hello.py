# import click
# import csv
# import json

# from pymongo import MongoClient

# @click.group()
# def dictionary():
#   print(1)

# @dictionary.command(name='create_bank_agency')
# @click.option('--count', default=1, help='Number of greetings.')
# # @click.argument('input', type=click.File('rb'))
# def create_bank_agency(count):
#   '''
#     CSV to JSON Conversion
#   '''
#   import ipdb; ipdb.set_trace()
#   print('2')
#   # csvfile = open(input)
#   # reader = csv.DictReader( csvfile )
#   # mongo_client=MongoClient() 
#   # db=mongo_client.october_mug_talk
#   # db.segment.drop()
#   # header= [ "S No", "Instrument Name", "Buy Price", "Buy Quantity", "Sell Price", "Sell Quantity", "Last Traded Price", "Total Traded Quantity", "Average Traded Price", "Open Price", "High Price", "Low Price", "Close Price", "V" ,"Time"]

#   # for each in reader:
#   #     row={}
#   #     for field in header:
#   #         row[field]=each[field]

#   #     db.segment.insert(row)



import click

@click.command()
def hello():
    click.echo('Hello World!')