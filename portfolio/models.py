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
    company_logo = models.ImageField(upload_to='company_icons/')
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
    isVoluntary = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"




class AchievementItem(models.Model):
    title = models.CharField(max_length=100)
    acheivementLink = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        blank=True,
        null=True
    )


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Categories(models.Model):
    section = models.ForeignKey(Section, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.section.name})"


class Skill(models.Model):
    category = models.ForeignKey(Categories, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills_icons/')
    active = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.category.name})"
    



class ProjectSection(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Project(models.Model):
    section = section = models.ForeignKey(ProjectSection, on_delete=models.CASCADE, default=1)  # ✅ if ID=1 exists

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/project_images/')
    description = models.TextField()
    link = models.URLField()
    tags = models.JSONField(default=list)  # or use a ManyToManyField to a Tag model
    youtube = models.URLField()
    def __str__(self):
        return self.name
    


class Publication(models.Model):
    name = models.CharField(max_length=500)
    year = models.DateField()
    name_url = models.URLField()
    authors = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    publication_name = models.CharField(max_length=100)
    publication_url = models.URLField()
    pdf_url = models.URLField()
    code = models.URLField()
    abstract = models.CharField(max_length=1000, default= "")
    
