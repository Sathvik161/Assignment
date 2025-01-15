import boto3
import base64
import json
import os

# Initialize the S3 client
s3 = boto3.client('s3')

# Set your S3 bucket name
BUCKET_NAME = os.environ.get('BUCKET_NAME', 'your-s3-bucket-name')

def lambda_handler(event, context):
    try:
        # Parse the event body
        body = json.loads(event['body'])
        file_name = body['fileName']
        file_content = body['fileContent']  # Base64-encoded content
        
        # Decode the Base64 file content
        decoded_file = base64.b64decode(file_content)
        
        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=decoded_file,
            ContentType='application/pdf'  # Adjust the Content-Type if needed
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully', 'fileName': file_name})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Missing parameter: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
