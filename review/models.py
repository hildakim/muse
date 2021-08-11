from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Review(models.Model):
  mt20id = models.CharField(max_length=10)
  title = models.CharField(max_length=50)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewers')
  rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  upload_date = models.DateTimeField()
  view_date = models.DateField()
  view_time = models.TimeField(null=True, blank=True)
  cast1 = models.CharField(max_length=10)
  cast2 = models.CharField(max_length=10, blank=True, null=True)
  body = models.TextField()
  image = models.ImageField(upload_to='review/%Y/%m/%d/', null=True, blank=True)
  image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 100)])

  class Meta:
    ordering = ['-upload_date']


# class ShowDetail(models.Model):
#   mt20id = models.CharField(max_length=20)
#   datefrom = models.CharField(max_length=10)
#   dateto = models.CharField(max_length=10)
#   facility = models.CharField(max_length=200)
#   poster = models.TextField()
#   genre = models.CharField(max_length=20)
#   state = models.CharField(max_length=20)
#   cast	= models.CharField(max_length=200)
#   crew	= models.CharField(max_length=50)
#   runtime	= models.CharField(max_length=20)
#   agelimit = models.CharField(max_length=50)
#   enterprise = models.CharField(max_length=50)
#   price = models.CharField(max_length=200)
#   story	= models.TextField()	
#   dateguidance = models.TextField()