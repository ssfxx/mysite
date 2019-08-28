from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from .models import BlogArticles

# Create your views here.


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/title.html",{"blogs":blogs})

def blog_article(request,article_id):
    template = get_template('blog/content.html')
    article = get_object_or_404(BlogArticles,id=article_id)  #引入该方法，当页面不存在是提示dose not exist
    pub = article.publish
    html = template.render({"article":article,"publish":pub})
    return HttpResponse(html)

