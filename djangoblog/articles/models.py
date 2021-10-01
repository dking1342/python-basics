from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User,default=None,on_delete=CASCADE)

    # method to show the title when retrieving from db
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]

