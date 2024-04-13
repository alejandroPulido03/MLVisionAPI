from django.urls import path


from .services.document_service import post_document
from base.views import get_document_score
from base.views import healthCheck


urlpatterns = [
    path('postDocument/', post_document, name='post_document'),
    path('document/<str:document_id>/',
         get_document_score, name='get_document_score'),

    path('health-check/', healthCheck),
]
