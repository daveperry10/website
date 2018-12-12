from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.files.images import ImageFile
from django.contrib.auth.models import AbstractUser
from django.db import models
from io import StringIO, BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.conf import settings
import os

class CustomUser(AbstractUser):
    # add additional fields in here
    #objects = MyManager
    city = models.CharField(max_length=250, null=True)
    picture = models.FileField(blank=True, null=True)
    birthday = models.DateField(null=True)
    bio = models.CharField(max_length=1000, null=True)
    color = models.CharField(max_length=50, null=True)
    #picture = models.ImageField('picture', upload_to='/media/', null=True, blank=True)

    def __str__(self):
        return self.email


class Pet(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    breed = models.CharField(max_length=250, blank=True)
    picture = models.FileField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('positivepets:detail', kwargs={'pk': self.pk, 'edit': '0'})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        overwrite the picture with a simple PIL save method in the media_root directory
        """
        if self.picture:
            super(Pet, self).save(*args, **kwargs)
            img = Image.open(self.picture)
            img.thumbnail((400, 400))
            file = os.path.join(settings.MEDIA_ROOT, self.picture.name)
            img.save(file, quality=60)
        else:
            super(Pet, self).save(*args, **kwargs)
        return

class Chat(models.Model):
    comment = models.CharField(max_length=2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('positivepets:chatmessage_create')

    def __str__(self):
        return self.comment

class Mail(models.Model):
    msg_id = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0,  related_name='as_sender')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0, related_name='as_recipient')
    status = models.IntegerField(default=0)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('positivepets:mail_create')

    def __str__(self):
        return self.message