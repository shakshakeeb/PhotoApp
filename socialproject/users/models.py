from django.db import models
from django.conf import settings

# model for representing user profiles
class Profile(models.Model):
    # a one-to-one relationship with the user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # an ImageField for uploading user profile photos (optional)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def _str_(self):
        # string representation of the profile (used in admin and elsewhere)
        return self.user.username
