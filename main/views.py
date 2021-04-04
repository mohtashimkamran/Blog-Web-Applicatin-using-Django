from django.shortcuts import render,get_object_or_404
from django.http import Http404
from main import models
# Create your views here.

def index(request):
    latest_articles = models.article.objects.all().order_by('-createdAt')[:10]
    
    context ={
        "latest_articles" : latest_articles
    }
    return render(request,'main\index.html',context)

def article(request,pk):
    article = get_object_or_404(models.article,pk=pk)
    context ={
        'article' : article 
    }
    return render(request,'main/article.html',context)

def author(request,pk):
    author= get_object_or_404(models.author,pk=pk)

    context={
        'author' : author
    }
    return render(request,'main/author.html',context)

def create_article(request):
    print(request.POST)
    author = models.author.objects.all()
    context={
        'authors' : author,
    }
    if request.method =="POST":
        article_data={
            'title':request.POST['title'],
            'content': request.POST['content']
        }

        article=models.article.objects.create(**article_data)
        author=models.author.objects.filter(pk=request.POST['author'])
        article.authors.set(author)

        context["success"]=True
    
    return render(request,'main/create_article.html',context)