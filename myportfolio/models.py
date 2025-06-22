from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import URLValidator

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class HomeSidebarInfo(models.Model):
    interestText = models.CharField(max_length=300)
    locaionText = models.CharField(max_length=300)
    emailText = models.EmailField(("example@gmail.com"), max_length=254)
    googleScholarLink = models.CharField(max_length=300)
    linkedInLink = models.CharField(max_length=300)
    twitterLink = models.CharField(max_length=300)
    githubLink = models.CharField(max_length=300)
    orcidLink = models.CharField(max_length=300)
    researchGateLink = models.CharField(max_length=300)

class EducationItem(models.Model):
    schoolNameText = models.CharField(max_length=300)
    schoolWebsiteLink = models.CharField(max_length=300, blank = True, null=True)
    degreeNameText = models.CharField(max_length=300)
    departmentNameText = models.CharField(max_length=300, blank = True, null=True)
    certificateLink = models.CharField(max_length=300, blank = True, null=True)
    durationText = models.CharField(max_length=300)
    gradeText = models.CharField(max_length=300, blank = True, null=True)
    transcriptLink = models.CharField(max_length=300, blank = True, null=True)

class JobExperienceItem(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_link = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        blank=True,
        null=True
    )
    department = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField()