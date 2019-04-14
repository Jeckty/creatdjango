from django.db import models

# Create your models here.
class classInfo(models.Model):
    cname = models.CharField(max_length=20)
    cdate = models.DateTimeField()



class studentInfo(models.Model):
    sname = models.CharField(max_length=20)
    ssex = models.BooleanField()
    scontent =models.CharField(max_length=200)
    sclass = models.ForeignKey("classInfo",on_delete=models.CASCADE)




