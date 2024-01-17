from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Model for representing a Post
class Post(models.Model):
    # A ForeignKey representing the user who created the post
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # An ImageField for uploading the post image
    image = models.ImageField(upload_to='images/%y/%m/%d')
    
    # A TextField for the post caption (optional)
    caption = models.TextField(blank=True)
    
    # A CharField for the post title
    title = models.CharField(max_length=200)
    
    # A SlugField to generate a URL-friendly version of the title
    slug = models.SlugField(max_length=200, blank=True)
    
    # A DateField for storing the creation date of the post
    created = models.DateField(auto_now_add=True)
    
    # A ManyToManyField to represent users who liked the post
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts_liked', blank=True)

    def __str__(self):
        # String representation of the Post (used in admin and elsewhere)
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate a slug for the post if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# Model for representing a Comment
class Comment(models.Model):
    # A ForeignKey representing the post to which the comment belongs
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    # A CharField for the comment body
    body = models.CharField(max_length=100)
    
    # A DateTimeField for storing the creation date of the comment
    created = models.DateTimeField(auto_now=True)
    
    # A CharField for the user who posted the comment
    posted_by = models.CharField(max_length=100)

    class Meta:
        # Define the default ordering for comments based on creation date
        ordering = ('created',)

    def __str__(self):
        # String representation of the Comment (used in admin and elsewhere)
        return self.body
