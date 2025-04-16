from django.db import models

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


