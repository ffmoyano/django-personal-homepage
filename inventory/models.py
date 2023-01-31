from django.db import models
from django.utils.safestring import mark_safe


class ProjectStatus(models.TextChoices):
    UPCOMING = "Upcoming"
    ACTIVE = "Active"
    PENDING = "Pending"
    FINISHED = "Finished"
    CANCELLED = "Cancelled"


class Base(models.Model):
    abstract = True
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=400, default='', blank=True)
    snapshot = models.ImageField(upload_to='images')
    visible = models.BooleanField(default=True)

    def display_image(self):
        if self.snapshot:
            return mark_safe(f'<img src = "{self.snapshot.url}" width = "300"/>')

    def display_list_image(self):
        if self.snapshot:
            return mark_safe(f'<img src = "{self.snapshot.url}" width = "100"/>')

    def __str__(self):
        return self.name


class Project(Base):
    status = models.CharField(choices=ProjectStatus.choices,
                              default=ProjectStatus.ACTIVE,
                              max_length=10)
    github = models.CharField(max_length=100, default='', blank=True)
    url = models.CharField(max_length=100, default='', blank=True)


class Element(Base):
    parent_project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
