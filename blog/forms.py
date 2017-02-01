from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('category', 'composer', 'label', 'image', 'title', 'text', 'rating', 'website')