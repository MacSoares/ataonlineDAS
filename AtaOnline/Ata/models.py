"""Models for Ata."""

from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.


class Student(User):
    """Student's docstring."""

    student_registration = models.IntegerField()
    objects = UserManager()


class Professor(User):
    """Professor's docstring."""

    professor_registration = models.IntegerField()
    formation = models.CharField(max_length=200)
    objects = UserManager()


class Notebook(models.Model):
    """Student's Notebook for class of Experimental Fisics."""

    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=250)
    grade = models.IntegerField(default=0)
