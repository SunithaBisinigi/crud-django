from django.shortcuts import render
from .serializers import BookSerializer
from .models import BooksModel
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response

class Booklistcreate(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class BooksDis(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)
