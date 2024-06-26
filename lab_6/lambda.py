import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket_start = s3.Bucket("s3start")
    bucket_finish = "s3finish"

    for obj in bucket_start.objects.filter(Prefix=''):
        copy_source = {'Bucket': "s3start", 'Key': obj.key}
        bucket_to_name = obj.key
        s3.meta.client.copy(copy_source, bucket_finish, bucket_to_name)