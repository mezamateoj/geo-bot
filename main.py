from bot import bot
import json


def lambda_handler(event, context):
    print('calling function...')
    try:
        print('here 1')
        bot()
        print('here 2')
        
        response = {
            'statusCode': 200,
            'body': json.dumps('Clock In')
            }
        
        return response

    except Exception as e:
        print(f'something went wrong {e}')
        
        response = {
            'statusCode': 400,
            'body': json.dumps('Could not clock in...'),
            'message': e
            }
        
        return response
