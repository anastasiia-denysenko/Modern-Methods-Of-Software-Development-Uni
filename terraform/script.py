import boto3
import uuid
import urllib


endpointurl = "http://localstack:4566"
def script(event,context):
        clientd = boto3.client('dynamodb',region_name='us-east-1',endpoint_url=endpointurl)
	bucket_name = event['Records'][0]['s3']['bucket']['name']
	key = event['Records'][0]['s3']['object']['key']
	key = urllib.parse.unquote_plus(key, encoding ='utf-8')
	message = "File got uploaded" + key + 'to the bucket' + bucket_name
	id_db = uuid.uuid4()
	idval = str(id_db)
	clientd.put_item(TableName='MYTerracottaTableNamePleaseWork',Item={'id':{'S':idval},'filename':{'S':key}})
	return "success"
