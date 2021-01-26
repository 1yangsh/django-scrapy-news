from django.views.generic import ListView

from django.shortcuts import render
from news.models import New




# Create your views here.
class NewsLV(ListView):
    model = New
    template_name = "news/news_all.html"
    context_object_name = "news" 


def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return False

    return True

