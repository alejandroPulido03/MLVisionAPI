from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from base.logic.document_logic import process_document


@csrf_exempt
def post_document(request):
    image = request.FILES.get('image')
    document_type = request.POST.get('document_type')
    process_document(image, document_type, None)
    return JsonResponse({'message': 'Document processed successfully'})
