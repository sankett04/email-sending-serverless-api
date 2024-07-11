import json
import boto3
from botocore.exceptions import ClientError
import os

def mock_send_email(receiver_email, subject, body_text):
    print(f"Mock email sent to: {receiver_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body_text}")
    return {'MessageId': 'mock-message-id'}

def send_email(event, context):
    try:
        # Parse the incoming JSON body
        body = json.loads(event['body'])
        
        # Extract email details
        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')
        
        # Validate inputs
        if not all([receiver_email, subject, body_text]):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'receiver_email, subject, and body_text are all required'})
            }

        if os.environ.get('IS_OFFLINE') == "true":
            # Use mock function when running offline
            response = mock_send_email(receiver_email, subject, body_text)
        else:
            # Create SES client
            ses_client = boto3.client('ses')

            # Specify the sender email (must be verified in SES)
            SENDER = "Your email"
            
            # Send the email
            response = ses_client.send_email(
                Destination={
                    'ToAddresses': [receiver_email],
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': 'UTF-8',
                            'Data': body_text,
                        },
                    },
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': subject,
                    },
                },
                Source=SENDER
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully', 'messageId': response['MessageId']})
        }
    
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e.response['Error']['Message'])})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }