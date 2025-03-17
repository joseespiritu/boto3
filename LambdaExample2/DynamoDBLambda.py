import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

    # DELETE ITEM
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')

    response = table.delete_item(
        Key={
            'id': 2
        }
    )

    print(response)

    # UPDATE DATA
    """ dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    table.update_item(
        Key={
            'id':1
        },
        UpdateExpression="set age = :g",
        ExpressionAttributeValues={
            ':g':45
        },
        ReturnValues="UPDATED_NEW"
    ) """

    # GET ITEM CONDITIONALLY
    """ dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    resp = table.query(
        KeyConditionExpression=Key('id').eq(2)
    )

    if 'Items' in resp:
        print(resp['Items'][0]) """

    # GET ITEMS
    """ db = boto3.resource('dynamodb')
    response = db.batch_get_item(
        RequestItems={
            'Users':{
                'Keys': [
                    {
                        'id':1
                    },
                    {
                        'id':2
                    },
                    {
                        'id':3
                    }
                ]
            }
        }
    )

    print(response) """

    #PUT OBJECTS ON TABLE
    """ db = boto3.resource('dynamodb')

    table = db.Table('Users')

    with table.batch_writer() as batch:
        batch.put_item(Item={'id':1,'name':'jose','age':'20'})
        batch.put_item(Item={'id':2,'name':'john','age':'25'})
        batch.put_item(Item={'id':3,'name':'abc','age':'30'}) """

    # CREATE TABLE
"""     dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName = 'Users',
        KeySchema = [
            {
                'AttributeName':'id',
                'KeyType':'HASH'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName':'id',
                'AttributeType':'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':3,
            'WriteCapacityUnits':3
        }
    )

    print("Table status ", table.table_status) """
    # END FILE
