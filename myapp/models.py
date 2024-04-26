from tkinter import Text
from tokenize import String

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db import models

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    studentId = models.CharField(max_length=12)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    grade_points = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=12)
    Correctedbyfacultyid = models.CharField(max_length=50,blank=False)
    CorrectedbyfacultyName = models.CharField(max_length=50,blank=False)

    class Meta:
        db_table = "Result_table"


# Create your models here.
class Register(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "Registrations"


class Student(models.Model):
    username = models.CharField(max_length=100)
    # Other student profile fields


class FeePayment(models.Model):
    studentId = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=20, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Fee payment details
    class Meta:
        db_table = "feepayments_table"


class StudentProfile(models.Model):
    id = models.AutoField(primary_key=True)
    studentId = models.CharField(max_length=12)
    full_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    year_of_study = models.IntegerField()  # You can use IntegerField for years of study
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=20)  # You can use CharField for contact number
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "studentprofile_table"

class EmployeeProfile(models.Model):
    employeeId = models.CharField(max_length=12, unique=True)  # Assuming employeeId should be unique
    full_name = models.CharField(max_length=100)
    date_of_join = models.DateField()  # Changed to DateField assuming it's a date
    email = models.EmailField(max_length=100, unique=True)  # Assuming email should be unique
    contact = models.CharField(max_length=20)  # Assuming contact number can have hyphens or spaces
    address = models.CharField(max_length=255)  # Increased max_length for address

    class Meta:
        db_table = "employeeprofile_table"


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT")) #tuple format
    department = models.CharField(max_length=20, blank=False,choices=department_choices)
    academic_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"))
    academicyear = models.CharField(max_length=10, blank=False,choices=academic_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
    Year = models.IntegerField(blank=False)
    coursecode=models.CharField(max_length=20,blank=False)
    coursetitle=models.CharField(max_length=100,blank=False)

class Ticket(models.Model):
    ticket = models.CharField(max_length=600,blank=False)
    studentid = models.CharField(max_length=20,blank=False)