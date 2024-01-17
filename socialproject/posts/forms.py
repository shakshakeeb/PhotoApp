from .models import Post, Comment
from django import forms

# Form for creating or updating a Post
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        # Specify the fields to include in the form
        fields = ('title', 'image', 'caption')

# Form for creating or updating a Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Specify the fields to include in the form
        fields = ('body', 'posted_by')
