from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.CharField(max_length=50, primary_key=True, null=False)
    first_name = models.CharField('First Name', max_length=50, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=50, blank=True)
    short_description = models.CharField('Short Description', max_length=100, blank=True)
    picture_url = models.CharField('Picture URL', max_length=300, blank=True)
    lang = models.CharField('Language', max_length=2, choices=(('en', 'English'), ('es', 'Spanish')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.lang)

class Quote(models.Model):
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    body = models.TextField('Body', blank=False)
    is_dayquote = models.BooleanField(default=False)
    lang = models.CharField('Language', max_length=2, choices=(('en', 'English'), ('es', 'Spanish')))
    created_at = models.DateTimeField(auto_now_add=True)



