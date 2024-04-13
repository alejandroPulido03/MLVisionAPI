from django.http import HttpResponse, JsonResponse
from .models import DocumentScore
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def get_document_score(request, document_id):
    document_score = get_object_or_404(DocumentScore, document_id=document_id)
    data = {
        'document_id': document_score.document_id,
        'score': document_score.score,
        # Si guardaste el texto y deseas retornarlo
        'document_text': document_score.document_text
    }
    return JsonResponse(data)


def healthCheck(request):
    return HttpResponse('ok')
