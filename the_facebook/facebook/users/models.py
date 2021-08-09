from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    biography = models.TextField(max_length = 200,blank=True)
    cover_image = models.ImageField(default='cover_default.jpg',upload_to='cover_pics')
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        cover = Image.open(self.cover_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)

        if cover.height > 300 or cover.width > 300:
            output_size = (600,800)
            cover.thumbnail(output_size)
            cover.save(self.cover_image.path)
