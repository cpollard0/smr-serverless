import os
import boto3
import json
import random
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table(os.getenv('tableName'))

def handle_decimal_type(obj):
  if isinstance(obj, Decimal):
      if float(obj).is_integer():
         return int(obj)
      else:
         return float(obj)
  raise TypeError

def get(gameId):
    response = table.get_item(
        Key={
            'gameId': gameId
        }
    )
    print(response)
    return response

def createSector(gameId, sectorId, width, height):

    linkUp = sectorId - width
    linkRight = sectorId + 1
    linkDown = sectorId + width
    linkLeft = sectorId - 1
    # If we're on the first row:
    if linkUp < 1:
        linkUp = width*height+linkUp
    if linkDown > width * height:
        linkDown = linkDown - width * height
    if sectorId % width == 0:
        linkRight = linkRight - width
    if linkLeft % width == 0:
        linkLeft = linkLeft + width

    sector = {
        'gameId': gameId,
        'sectorId': sectorId,
        'linkUp': linkUp,
        'linkRight': linkRight,
        'linkDown': linkDown,
        'linkLeft': linkLeft
    }

    portProbability = .2 # TODO: Make variable based on the galaxy

    if random.random() <= portProbability:
        level = random.randint(1,9)
        sector['port'] = { # TODO: get goods for buy/sell
            'race': random.randint(1,10),
            'level': level
        }

    response = table.put_item(
        Item=sector
    )
    return response

def handler(event, context):

    width = 10 # TODO: Get from event
    height = 10 # TODO: Get from event
    for n in range(width*height):
        createSector(1, n + 1, width, height)
    print (event)