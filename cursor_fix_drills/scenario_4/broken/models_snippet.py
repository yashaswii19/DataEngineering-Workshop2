from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateTimeField('Release Date')
    blog_time = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True)
