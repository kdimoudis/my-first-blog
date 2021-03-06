from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Composer(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    category = models.ForeignKey('Category',null=True)
    composer = models.ForeignKey('Composer',null=True)
    label = models.ForeignKey('Label',null=True)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    website = models.URLField('Website', null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


