from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # AbstractUser 상속받아 유저 모델 확장
    nickname = models.CharField(max_length=100, default="익명의사자")
    birth = models.DateField(max_length=10, null=True, blank=True)
    