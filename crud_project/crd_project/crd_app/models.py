from django.db import models

# Create your models here.


class student_deatils(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    photo =models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    class Meta:
        verbose_name_plural = "Student Deatils"
    def __str__(self):
        return self.name
    

