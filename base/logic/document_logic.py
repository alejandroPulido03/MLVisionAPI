import os

from django.http import HttpResponse, JsonResponse
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'


def process_document(file, document_type, user):
    client = vision.ImageAnnotatorClient()
    request = {
        'image': {
            'content': file.read()
        },
        'features': [
            {
                'type_': 'TEXT_DETECTION'
            }
        ]
    }
    res = client.annotate_image(request=request)
    print(res)


def store_document(file, user):
    pass


def send_request(file):
    pass
