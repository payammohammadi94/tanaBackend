from dataclasses import fields
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment','rate']
        
class ReplayForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']