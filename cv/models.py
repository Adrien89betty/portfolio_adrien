# cv/models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    logo = models.CharField(
        max_length=100,
        help_text="File name in cv/static/cv/images/"
    )

    def __str__(self):
        return self.name



class Certification(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date_obtained = models.DateField()
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='certification_logos/', blank=True, null=True)

    def __str__(self):
        return self.title


class CV(models.Model):
    file = models.FileField(upload_to='cv_files/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CV updated at {self.updated_at}"
