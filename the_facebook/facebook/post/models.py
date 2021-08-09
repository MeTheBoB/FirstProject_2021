from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from users import models as user_model

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(blank=True,max_length=80)
    message = models.TextField(blank=True)
    image_post = models.ImageField(blank=True,upload_to='post_image')
    date_posted = models.TimeField(default = timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail',kwargs={'pk':self.pk})




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=80)
    date_posted = models.TimeField(default = timezone.now)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return rever('post:post_detail',kwargs={'pk':'self.pk'})
