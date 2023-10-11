from django.db import models

# Create your models here.
class Monument(models.Model):
    name=models.CharField(max_length=250)
    about=models.TextField()
    image=models.ImageField(upload_to='pics')
    year=models.IntegerField()


