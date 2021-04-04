from django.db import models

# Create your models here.

class author(models.Model):
    name = models.CharField(null=True,max_length=256)
    def __str__(self):
        return self.name
    articles =models.ManyToManyField('article')

class article(models.Model):
    title=models.CharField(null=True,max_length=256)
    createdAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    authors=models.ManyToManyField('author')
    
    def __str__(self):
        return self.title 