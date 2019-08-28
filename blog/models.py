from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300,verbose_name="博客标题")
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title  #直接返回标题 python3 都使用__str__  python2一般使用__unicode__

    #def __unicode__(self):
    #   return self.title
    #like this:BlogArticles object (1)
