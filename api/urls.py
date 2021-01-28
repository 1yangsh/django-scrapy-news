from django.urls import path, include
from api.views import NewsViewSet

app_name = 'api'

# news 전체 보기
news_list = NewsViewSet.as_view({'get': 'list'})
# news 상세 보기
news_detail = NewsViewSet.as_view({'get': 'retrieve'})


urlpatterns = [
    path('ITnews/', news_list, name='news_list'),
    path('ITnews/<int:pk>', news_detail, name='news_detail'),
]