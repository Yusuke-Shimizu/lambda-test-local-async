import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import logging
import jsonpickle
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

def handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))

    sqs_client = boto3.client("sqs")
    
    queue_url = "https://sqs.ap-northeast-1.amazonaws.com/889119567707/LambdaTestLocalAsyncStack-dev-Queue4A7E3555-FUIEAJMZLVUG"
    
    response = sqs_client.send_message(QueueUrl=queue_url, MessageBody="message 1")
    logger.info('## SQS RESPONSE\r' + jsonpickle.encode(response))
    # print(response)
    return {
        'statusCode': 200,
        'body': 'Lambda was invoked successfully.'
    }
