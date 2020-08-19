from django.db import models

# Create your models here.


class Incentive(models.Model):
    content = models.TextField()
    source = models.CharField(max_length=125)


class Request(models.Model):
    content = models.TextField()
    source = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
    # 0 = pendding | 1 = accepted | 2 = rejected
    status = models.IntegerField(default=0)
