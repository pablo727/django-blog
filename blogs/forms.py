from django import forms

from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': ''}

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['posts']
        labels = {'posts': ''}
        widgets = {'posts': forms.Textarea(attrs={'cols': 80})}