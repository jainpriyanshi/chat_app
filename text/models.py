from django.conf import settings
from django.db import models
from django.utils import timezone


class Text(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    img=models.ImageField(upload_to='images/', blank=True)
    




    def post(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.message

class Profile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    motto = models.CharField(max_length=100 )

    def post(self):
        self.save()

    def __str__(self):
        return self.message