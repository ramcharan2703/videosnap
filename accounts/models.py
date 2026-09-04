from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=500)
    city=models.TextField(blank=True,null=True)
    state=models.TextField(blank=True,null=True)
    district=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile/',blank=True,null=True)

    def __str__(self):
        return self.user.username
#education
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="educations")

    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)

    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

    grade = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.degree

#experience
class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return self.company

        #skill
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")

    skill_name = models.CharField(max_length=100)

    LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    level = models.CharField(max_length=20, choices=LEVELS)

    def __str__(self):
        return self.skill_name

#Certificate

class Certificate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="certificates")

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    issue_date = models.DateField()

    certificate_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    #projects

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")

    title = models.CharField(max_length=200)

    description = models.TextField()

    technologies = models.CharField(max_length=300)

    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

#achievements

class Achievement(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="achievements")

    title = models.CharField(max_length=200)
    description = models.TextField()

    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

#language

class Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="languages")

    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language

#social links
class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="social_links")

    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.platform

#intrests

class Interest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="interests")

    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest

#contacts

class Contact(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)
    email = models.EmailField()

    website = models.URLField(blank=True)

    def __str__(self):
        return self.email