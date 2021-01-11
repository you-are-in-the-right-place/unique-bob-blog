from django.db import models
from django.utils import timezone

# Create your models here.
class Announce(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    attach = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Member(models.Model):
    D = 'D'
    S = 'S'
    R = 'R'
    CHOICE = (
        (D, "Director"),
        (S, "Senior"),
        (R, "Researcher"),
    )
    type = models.CharField(max_length=20, choices=CHOICE, default='R')
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    thumb = models.URLField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
