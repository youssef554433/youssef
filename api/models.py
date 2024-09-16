from django.db import models
from datetime import datetime
import uuid



    # Create your models here.




class Chapter(models.Model):
    numberchapter =  models.IntegerField()
    imagemanga = models.ImageField(upload_to='imagemangachapter',blank=True, null=True)
    namemanga = models.ForeignKey('Manga', related_name='imagechapter',on_delete=models.PROTECT)
    datepost = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.numberchapter








class Manga(models.Model):
    x=[
        ('manga','مانجا يابانية'),
        ('manho','مانهو كورية')
    ]

    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key = True , unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='img')
    typee = models.CharField(max_length=70,blank=True, null=True,choices=x)
    aounther = models.CharField(max_length=100,blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    reviews = models.DecimalField(max_digits=3, decimal_places=2,blank=True, null=True)
    chapter = models.ManyToManyField(Chapter,related_name='chapter',blank=True, null=True)


    def __str__(self):
        return self.name








class ImageChapter(models.Model):
    chapters = models.ForeignKey(Chapter, related_name='imageschapter', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='imaaa')




class Cartitem(models.Model):
    cartmanga = models.OneToOneField(Manga,on_delete=models.PROTECT)





    
    


    