from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', NewsLV.as_view(), name='index'),
    # path('search/', SearchFormView.as_view(), name='search'),
]