from django import forms

from home.models import Comment





class NewsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

