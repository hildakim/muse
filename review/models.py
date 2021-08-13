from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Review(models.Model):
  mt20id = models.CharField(max_length=10)
  title = models.CharField(max_length=50)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviewers')
  rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  upload_date = models.DateTimeField()
  view_date = models.DateField()
  view_time = models.TimeField()
  cast1 = models.CharField(max_length=10, blank=True, null=True)
  cast2 = models.CharField(max_length=10, blank=True, null=True)
  body = models.TextField()
  image = models.ImageField(upload_to='review/%Y/%m/%d/', null=True, blank=True)
  image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 200)])

  def __str__(self):
    return self.mt20id

  class Meta:
    ordering = ['-upload_date']


# class SortCondition(models.Model):
#   TITLE_CHOICES = list(Review.objects.values_list('title', 'title').order_by('title').distinct())
#   cast1_list = list(Review.objects.values_list('cast1', 'cast1').order_by('cast1').distinct().exclude(cast1__isnull=True).exclude(cast1__exact='')) 
#   cast2_list = list(Review.objects.values_list('cast2', 'cast2').order_by('cast2').distinct().exclude(cast2__isnull=True).exclude(cast2__exact=''))
#   DATE_CHOICES = list(Review.objects.values_list('view_date', 'view_date').order_by('view_date').distinct())
#   CAST_CHOICES = cast1_list + cast2_list
#   TIME_CHOICES = list(Review.objects.values_list('view_time', 'view_time').order_by('view_time').distinct())

#   title = models.CharField(max_length=50,choices=TITLE_CHOICES, blank=True)
#   cast = models.CharField(max_length=10, choices=CAST_CHOICES, blank=True)
#   view_date = models.DateField(choices=DATE_CHOICES, blank=True)
#   view_time = models.TimeField(choices=TIME_CHOICES, blank=True)

#   title2 = models.ForeignKey(Review, on_delete=CASCADE, blank=True)




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