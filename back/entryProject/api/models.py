from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
import enum


class User(AbstractUser):

    dateOfBirth = models.DateField(verbose_name="Date of birth")


class CompanyType(enum.Enum):

    individualEntrepreneurship = "Individual Entrepreneurship"
    limitedLiabilityPartnership = "Limited Liability Partnership"
    corporation = "Corporation"

    @classmethod 
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Entrepreneur(models.Model):

    first_name = models.CharField(verbose_name="First name", max_length=64)
    last_name = models.CharField(verbose_name="Last name", max_length=64)
    email = models.EmailField(verbose_name="Email", max_length=64)
    tel = models.CharField(verbose_name="Telephone number", max_length=12)


class Company(models.Model):

    name = models.CharField(verbose_name="Name")
    type = models.CharField(verbose_name="Type", choices=CompanyType.choices())
    logo = models.URLField(verbose_name="Logo")
    owner = models.ForeignKey(Entrepreneur, verbose_name="Owner", on_delete=models.CASCADE)
    foundingDate = models.DateField(verbose_name="Founding date")
    lastModifiedDate = models.DateField(verbose_name="Last modified date", auto_now=True)


class Review(models.Model):

    rating = models.IntegerField(verbose_name="Rating", choices=(1, 2, 3, 4, 5))
    reviewContent = models.TextField(verbose_name="Review content")
    date = models.DateField(verbose_name="Date of leaving the review", auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="Author", on_delete=CASCADE)
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=CASCADE)
