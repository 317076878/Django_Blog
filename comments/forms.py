'''
Created on 2019年10月22日

@author: 周礼佟win10
'''
from django import forms
from .models import Comment
 
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
