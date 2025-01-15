import json

def lambda_handler(event, context):
    # Extract numbers from the event body
    try:
        body = json.loads(event['body'])
        num1 = body['num1']
        num2 = body['num2']
        
        # Validate input
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Inputs must be numbers")
        
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except (KeyError, ValueError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }
