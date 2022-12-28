from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/<pk>/', getproduct, name='getproduct')
    # path('ajaxjson', ajaxindex, name='ajaxindex'),

]