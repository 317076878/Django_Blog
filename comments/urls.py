'''
Created on 2019年10月22日

@author: 周礼佟win10
'''
from django.urls import path
 
from . import views
 
app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
