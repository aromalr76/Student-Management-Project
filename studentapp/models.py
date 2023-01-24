from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city_name}'

class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course_name}'

class Student(models.Model):
    sname = models.CharField(max_length=50)
    sage = models.IntegerField()
    sphno = models.BigIntegerField()
    scity = models.ForeignKey(City,on_delete=models.CASCADE)
    scourse = models.ForeignKey(Course,on_delete=models.CASCADE)
