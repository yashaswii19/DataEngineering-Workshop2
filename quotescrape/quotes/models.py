from django.db import models

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    tags = models.TextField()

    def __str__(self):
        return self.quote
