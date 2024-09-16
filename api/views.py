from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class Api_Manga(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = Manga_Serializer


class Api_Chapter(ModelViewSet):
    queryset = Chapter.objects.all()[0:100]
    serializer_class = Chapter_Serializer


class Api_ImageChapter(ModelViewSet):
    queryset = ImageChapter.objects.all()[0:100]
    serializer_class = ImageChapter_Serializer



class Api_Cartitem(ModelViewSet):
    queryset = Cartitem.objects.all()[0:20]
    serializer_class = Cartitem_Serializer
     

