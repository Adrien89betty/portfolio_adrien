from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.JSONField()
    github_link = models.URLField()
    demo_link = models.URLField(blank=True, null=True)
    image = models.CharField(
        max_length=100,
        blank=True, null=True,
        help_text="File name in project/static/project/images/"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
