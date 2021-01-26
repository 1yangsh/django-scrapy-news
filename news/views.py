from django.views.generic import ListView, DetailView

from django.shortcuts import render
from news.models import New




# Create your views here.
class NewsLV(ListView):
    model = New
    template_name = "news/news_all.html"
    context_object_name = "news" 


class NewsDV(DetailView):
    model = New

