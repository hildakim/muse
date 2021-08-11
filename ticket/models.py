from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Ticket(models.Model):
    ticket = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    date = models.DateTimeField()
    contents = models.TextField()
    image = models.ImageField(upload_to='ticket/', blank=True, null=True)
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(250, 230)])
  
    def __str__(self):
        return self.ticket    
    def summary(self):
        return self.contents[:100]
