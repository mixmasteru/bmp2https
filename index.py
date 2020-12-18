import base64


def handler(event, context):
    with open("falcon9_pil.bmp", "rb") as image:
        f = image.read()
        b = bytearray(f)

    return respond(b)


def respond(buf):
    return {'isBase64Encoded': True,
            'statusCode': 200,
            'headers': {'Content-Type': 'image/bmp'},
            'body': base64.b64encode(buf).decode('UTF-8')}
