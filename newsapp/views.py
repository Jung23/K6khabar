from django.shortcuts import render
from .models import PostModel, CategoryModel
import datetime

def index(request):
    posts = PostModel.objects.all()[:10]
    categories = CategoryModel.objects.all()[:5]
    featured_post = posts[0]
    context = {
        'posts' : posts,
        'categories': categories,
        'featured_post': featured_post
    }
    return render(request, 'newsapp/index.html', context)


def detail(request, id):
    post = PostModel.objects.filter(id=id).first()
    categories = CategoryModel.objects.all()[:5]
    context = {
        'post': post,
        'categories': categories
    }
    return render(request,'newsapp/detail.html', context)


def categorynews(request, id):
    category = CategoryModel.objects.filter(id=id).first()
    if category:
        posts= PostModel.objects.filter(category=category)
        categories = CategoryModel.objects.all()[:5]
        context = {
            'posts': posts,
            'categories': categories
        }

        return render(request,'newsapp/index.html', context)
    else:
        return render(request, 'newsapp/error404.html')
