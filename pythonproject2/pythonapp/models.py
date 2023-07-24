from django.db import models

# Create your models here.
class places(models.Model):
    names=models.CharField(max_length=250)
    image=models.ImageField(upload_to="pics")
    desc=models.TextField()

class individuals(models.Model):
    name=models.CharField(max_length=250)
    images=models.ImageField(upload_to="pictures")
    descr=models.TextField()



    def __str__ (self):
        return self.name

