from django.db import models

# Create your models here.
class Furniture(models.Model):
    title = models.CharField(max_length=68)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Rom(models.Model):
    headline = models.CharField(max_length=68)
    furnitures = models.ManyToManyField(Furniture)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline