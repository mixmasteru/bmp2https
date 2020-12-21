import base64
import os
from boto3 import client


def handler(event, context):
    b = ""
    if event is not None and event['pathParameters']['bucket']:
        bucket = event['pathParameters']['bucket']
        path = s3bmp(bucket)

        with open(path, "rb") as image:
            f = image.read()
            b = bytearray(f)

    return respond(b)


def s3bmp(bucket_name):
    s3 = client("s3")
    response = s3.list_objects_v2(
        Bucket=bucket_name,
        Prefix='dither',
        MaxKeys=100)

    folder = response['Contents'][0]['Key']
    key = response['Contents'][1]['Key']
    download_path = '/tmp/' + key
    folder = '/tmp/' + folder
    if not os.path.exists(folder):
        os.makedirs(folder)
    s3.download_file(bucket_name, key, download_path)

    return download_path


def respond(buf):
    return {'isBase64Encoded': True,
            'statusCode': 200,
            'headers': {'Content-Type': 'image/bmp'},
            'body': base64.b64encode(buf).decode('UTF-8')}
