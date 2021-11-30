from django.db import models
class postdata(models.Model):
    data = models.TextField()
    host = models.CharField(max_length=1000,default="none")