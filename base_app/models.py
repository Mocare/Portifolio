from django.db import models
from django.db import models
# Create your models here.
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.profile.name}"

class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')

    def __str__(self):
        return f"{self.title} - {self.profile.name}"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.institution} - {self.profile.name}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} - {self.profile.name}"

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.profile.name}"

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.profile.name}"

class Testimonial(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='testimonials')
    name = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return f"Testimonial by {self.name} - {self.profile.name}"
