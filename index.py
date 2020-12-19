import base64
from boto3 import client


def handler(event, context):
    b = ""
    if event.pathParameters.bucket:
        bucket = event.pathParameters.bucket
        s3bmp(bucket)
    else:
        with open("falcon9_pil.bmp", "rb") as image:
            f = image.read()
            b = bytearray(f)

    return respond(b)


def s3bmp(bucket_name):
    conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
    for key in conn.list_objects(Bucket=bucket_name)['Contents']:
        print(key['Key'])


def respond(buf):
    return {'isBase64Encoded': True,
            'statusCode': 200,
            'headers': {'Content-Type': 'image/bmp'},
            'body': base64.b64encode(buf).decode('UTF-8')}
