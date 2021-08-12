from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Ticket(models.Model):
    ticket = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author', null=True)
    date = models.DateTimeField()
    contents = models.TextField()
    image = models.ImageField(upload_to='ticket/', blank=True, null=True)
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(250, 230)])
  
    def __str__(self):
        return self.ticket    
    def summary(self):
        return self.contents[:100]
