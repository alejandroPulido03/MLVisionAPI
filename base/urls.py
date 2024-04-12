from django.urls import path

from .services.document_service import post_document

urlpatterns = [
    path('postDocument/', post_document)
]
