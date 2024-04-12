import os

from django.http import HttpResponse, JsonResponse
from google.cloud import vision
import re

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
    response_text = res.text_annotations[0].description
    print(response_text)
    print(calcular_confianza_score(response_text))


def calcular_confianza_score(texto):
    patterns = {
        'header': re.compile(r'CÉDULA\s+DE\s+CIUDADANÍA', re.IGNORECASE),
        'republica': re.compile(r'REPÚBLICA\s+DE\s+COLOMBIA', re.IGNORECASE),
        'nuip': re.compile(r'NUIP\s+\d{1,10}'),  
        'nombres_apellidos': re.compile(r'Nombres?|Apellidos?', re.IGNORECASE),  
        'fecha': re.compile(r'\d{1,2}\s+\w+\s+\d{4}', re.IGNORECASE),  
        'sexo': re.compile(r'Sexo\s+[MF]', re.IGNORECASE),  
        'lugar_nacimiento': re.compile(r'Lugar\s+de\s+nacimiento', re.IGNORECASE),
        'fecha_expedicion': re.compile(r'Fecha\s+y\s+lugar\s+de\s+expedición', re.IGNORECASE),
        'fecha_expiracion': re.compile(r'Fecha\s+de\s+expiración', re.IGNORECASE)
    }
    weights = {
        'header': 0.2,  
        'republica': 0.2,  
        'nuip': 0.2,
        'nombres_apellidos': 0.1,  
        'fecha': 0.1,  
        'sexo': 0.1,  
        'lugar_nacimiento': 0.05,  
        'fecha_expedicion': 0.05,  
        'fecha_expiracion': 0.05  
    }
    score = 0
    
    for key, pattern in patterns.items():
        if pattern.search(texto):
            score += weights[key]

    return (score)
    

def store_document(file, user):
    pass


def send_request(file):
    pass
