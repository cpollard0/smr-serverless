import boto3
from botocore.exceptions import ClientError

import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('smr-classic-cmp-api-test-sectorTable-3TOT961U5AKV')  # TODO: Make into a lookup

def handle_decimal_type(obj):
  if isinstance(obj, Decimal):
      if float(obj).is_integer():
         return int(obj)
      else:
         return float(obj)
  raise TypeError
  
def get(gameId, sector_id):
    response = table.get_item(
        Key={
            'gameId': gameId,
            'sectorId': sector_id
        }
    )
    print(response)
    return response

def updatePort(game_id, sector_id, body):
    port = {"port": body } 
    response = table.update_item(
        Key={
            'gameId': int(game_id),
            'sectorId': int(sector_id)
        },
        UpdateExpression="SET port_info=(:i)",
        ExpressionAttributeValues={
            ':i': body
        }
    )  
    return response

def updatePortGood(game_id, sector_id, body): 
    del body['sectorId']
    del body['gameId']  
    portGood = {"portGoods":{str(body['goodId']):body}} 
    
    try:
        response = table.update_item(
            Key={
                'gameId': int(game_id),
                'sectorId': int(sector_id)
            }, 
            
            UpdateExpression="SET portGoods.#goodNumber=:i", 
            ExpressionAttributeNames={
                '#goodNumber' : str(body['goodId']),
            },
            ExpressionAttributeValues={
               ':i': portGood['portGoods'][str(body['goodId'])]
            }
        )  
    
    except ClientError as e:
        if e.response['Error']['Code'] == 'ValidationException':
            response = table.update_item(
            Key={
                'gameId': int(game_id),
                'sectorId': int(sector_id)
            },             
            UpdateExpression="SET portGoods=:i", 
            ExpressionAttributeValues={
                ':i': portGood['portGoods'] 
            }
        )  
    return response

def createUpdate(gameDetails):
    response = table.put_item(
        Item=gameDetails
    ) 
    return response

def handler(event, context): 
    print (event)
    if event['resource'] == "/sector/{gameId}/{sectorId}/port": 
        response = updatePort(event['pathParameters']['gameId'], 
            event['pathParameters']['sectorId'],
            json.loads(event['body']))
    elif event['resource'] == "/sector/{gameId}/{sectorId}/port/good": 
        response = updatePortGood(event['pathParameters']['gameId'], 
            event['pathParameters']['sectorId'],
            json.loads(event['body']))
        
    else:
        if event['httpMethod'] == 'GET':
            response = get(3)
        else:
            body = json.loads(event['body'])
            print(body)
            response = createUpdate(body)
    return {
        "statusCode": 200,
        "body": json.dumps(response, default=handle_decimal_type)
    }