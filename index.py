import base64
import os
from boto3 import client
from PIL import Image


def handler(event, context):
    b = "".encode()
    bmpid = 1
    if event is not None and event['pathParameters']['bucket']:
        bucket = event['pathParameters']['bucket']
        if 'bmpid' in event['pathParameters']:
            bmpid = int(event['pathParameters']['bmpid'])

        path = s3bmp(bucket, bmpid)

        with open(path, "rb") as image:
            f = image.read()
            b = bytearray(f)

    return respond(b)


def s3bmp(bucket_name, bmpid):
    download_path = ""
    s3 = client("s3")
    response = s3.list_objects_v2(
        Bucket=bucket_name,
        Prefix='dither',
        MaxKeys=100)

    folder = response['Contents'][0]['Key']
    cnt = response['KeyCount']
    if cnt > bmpid:
        key = response['Contents'][bmpid]['Key']
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
