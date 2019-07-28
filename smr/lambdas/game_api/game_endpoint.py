import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('smr-classic-cmp-api-test-gameTable-RM16Q456LPVU')  # TODO: Make into a lookup

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

def createUpdate(gameDetails):
    response = table.put_item(
        Item=gameDetails
    ) 
    return response

def handler(event, context): 
    print (event)
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