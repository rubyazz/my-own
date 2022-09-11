from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    date = models.DateField()
    image = models.ImageField(null=True)

    def get_absolute_url(self):
        return reverse('view_posts', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    link = models.URLField(max_length=2000, null=True)

    def __str__(self):
        return self.name
