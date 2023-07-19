from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self): 
        return self.title
    

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.PositiveIntegerField()
    email = models.EmailField(max_length=256)
    field_of_study = models.ForeignKey(Department, on_delete=models.CASCADE)
    gpa = models.FloatField()
    image = models.ImageField(upload_to='images/')
    


    def __str__(self): 
        return f'Students: {self.first_name} {self.last_name}'