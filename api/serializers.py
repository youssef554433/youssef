from rest_framework import serializers
from .models import *


    




class ImageChapter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ImageChapter
        fields = ['id','chapters','image']




class Chapter_Serializer(serializers.ModelSerializer):
    namemanga = serializers.StringRelatedField()
    imageschapter = ImageChapter_Serializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=100000,allow_empty_file=False,use_url=False),
        write_only=True
    )
    class Meta:
        model = Chapter
        fields = ['id','numberchapter','imagemanga','imageschapter','uploaded_images','namemanga','datepost']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        chapter = Chapter.objects.create(**validated_data)
        for image in uploaded_images:
            ImageChapter.objects.create(chapters=chapter,image=image)
        return chapter


        



class Manga_Serializer(serializers.ModelSerializer):
    chapter = Chapter_Serializer(read_only=True,many=True)
    class Meta:
        model = Manga
        fields = ['id','name','image','description','typee','date','aounther','reviews','chapter']




class Cartitem_Serializer(serializers.ModelSerializer):
    cartmanga = Manga_Serializer(read_only=True)
    class Meta:
        model = Cartitem
        fields = ['id','cartmanga']
        


    
    

    

        

    
    
    


    