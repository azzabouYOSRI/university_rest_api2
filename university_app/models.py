from django.db import models

# Create your models here.
from datetime import date

from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    birthDate = models.DateField(default=date(2003, 1, 1), null=False, blank=False)


class Grade(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50)
    numberOfStudents = models.IntegerField()
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField()
    workEmail = models.EmailField()
    personalEmail = models.EmailField()
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    birthDate = models.DateField(default=date(2003, 1, 1), null=False, blank=False)
    weeklyHours = models.IntegerField()


class Course(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses', null=False, blank=False)
    students = models.ManyToManyField(Student, related_name='courses', blank=False)
    grades = models.ManyToManyField(Grade, related_name='courses', blank=False)


class Session(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    courses = models.ManyToManyField(Course, related_name='sessions', blank=False)
    startTime = models.DateTimeField(null=False, blank=False)
    endTime = models.DateTimeField(null=False, blank=False)
    room = models.CharField(max_length=50, null=False, blank=False)
    goal = models.CharField(max_length=100, null=False, blank=False)
    summary = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)


class Attendance(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='attendances', null=False, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances', null=False, blank=False)
    motif = models.CharField(max_length=100, null=False, blank=False)
    justification = models.CharField(max_length=100, null=False, blank=False)


def __str__(self):
    return self.name
