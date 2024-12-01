from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
        labels = {'title': ''}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}