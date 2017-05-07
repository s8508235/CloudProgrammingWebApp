import boto3
# client = boto3.client('sqs')
sqs = boto3.setup_default_session(region_name='us-east-1')
sqs = boto3.resource('sqs')
import os
import urllib
#https://sqs.us-east-1.amazonaws.com/946681148855/awseb-e-kyfwgbat8d-stack-AWSEBWorkerQueue-NVSGJDJD1J0O os.environ['SQS_URL']
def get_image(filename):
	filename = urllib.unquote(filename)
	file_message = "{\"url\":\""+filename+"\"}"
	queue = sqs.Queue(os.environ['SQS_URL'])
	response = queue.send_message(
		MessageBody=file_message)
	file_split = filename.split("/")
	return os.environ['S3_BUCKET']+file_split[len(file_split)-1]