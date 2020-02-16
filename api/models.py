from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField('First Name', max_length=50, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=50, blank=True)
    short_description = models.CharField('Short Description', max_length=100, blank=True)
    picture_url = models.CharField('Picture URL', max_length=300, blank=True)


