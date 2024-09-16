from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter
#from rest_framework_nested import routers

router = DefaultRouter()


router.register('manga',Api_Manga)
router.register('chapter',Api_Chapter)
router.register('imagechapter',Api_ImageChapter)
router.register('cartitem',Api_Cartitem)





urlpatterns = [
    path('',include(router.urls)),
   
]