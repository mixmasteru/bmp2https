import json
import datetime
import base64
from PIL import Image
import io


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    img = Image.open("falcon9_pil.bmp")  # .convert("RGB")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='BMP')
    img_byte_arr = img_byte_arr.getvalue()

    return respond(img_byte_arr)

    # return {'statusCode': 200,
    #        'body': json.dumps(data),
    #        'headers': {'Content-Type': 'application/json'}}


def respond(img_byte_arr):
    return {'isBase64Encoded': False,
            'statusCode': 200,
            'headers': {'Content-Type': 'image/bmp'},
            'body': base64.b64encode(img_byte_arr).decode('UTF-8')}
