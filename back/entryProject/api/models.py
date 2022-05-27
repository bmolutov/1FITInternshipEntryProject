from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
import enum
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validateAge(dateOfBirth):
    age = (datetime.now().year - dateOfBirth.year)
    print(age)
    if age < 16:
        raise ValidationError(
            _('You are under 16 years of age!'),
            params={'dateOfBirth': dateOfBirth},            
        ) 


class CustomUser(AbstractUser):

    dateOfBirth = models.DateField(
        verbose_name="Date of birth", 
        default=datetime.today,
        validators=[validateAge],
        )


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

    name = models.CharField(verbose_name="Name", max_length=64)
    type = models.CharField(verbose_name="Type", choices=CompanyType.choices(), max_length=128)
    logo = models.URLField(verbose_name="Logo")
    owner = models.ForeignKey(Entrepreneur, verbose_name="Owner", on_delete=models.CASCADE)
    foundingDate = models.DateField(verbose_name="Founding date")
    lastModifiedDate = models.DateField(verbose_name="Last modified date", auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'


class Review(models.Model):

    RATES = (
        (1, "bad"), 
        (2, "unsatisfactory"), 
        (3, "satisfactorily"), 
        (4, "good"), 
        (5, "great")
    ) 
    rating = models.IntegerField(verbose_name="Rating", choices=RATES)
    reviewContent = models.TextField(verbose_name="Review content")
    date = models.DateField(verbose_name="Date of leaving the review", auto_now_add=True)
    author = models.ForeignKey(CustomUser, verbose_name="Author", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)
