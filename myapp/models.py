from django.db import models

# Create your models here.
class signmodel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=12)

class mynotes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='MyNotes')
    desc=models.TextField()

class contactus(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=25)
    email=models.EmailField()
    msg=models.TextField()