import boto3

url = boto3.client('s3').generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': 'dog-book-direct-test', 'Key': '3974752c-9a38-44f4-a9e3-2b1032920fcf.jpg'},
    ExpiresIn=15)
print(url)

