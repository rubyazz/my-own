from django.shortcuts import render
from django.views.generic import DetailView
from .models import *





def home(request):
    return render(request, 'main.html')


def portfolio(request):
    Portfolios = Portfolio.objects.all()
    context = {'portfolios': Portfolios}
    return render(request, 'portfolio.html',context)


def blog(request):
    Posts = Post.objects.all()
    context = {'posts': Posts}
    return render(request, 'blog.html', context)


def about(request):
    return render(request, 'about.html')


class ViewPost(DetailView):
   model = Post
   context_object_name = 'post'
   template_name = 'view_posts.html'





