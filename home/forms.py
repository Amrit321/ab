from django import forms

from home.models import Comment





class NewsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'post']
    # name = forms.CharField(label="name", max_length=255)
    # email = forms.EmailField(label="email")
    # body = forms.Textarea(label = "body")
    # post = forms.IntegerField(label="post")
