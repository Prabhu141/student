from django.db import models

class Student(models.Model):
    sid=models.CharField(max_length=20)
    name=models.TextField(max_length=100,blank=True)
    age=models.IntegerField(max_length=100,blank=True)
    standard=models.IntegerField(max_length=10,blank=True)

    def __str__(self):
        return "%s" %(self.name)
    
    class Meta:
        db_table="student"
