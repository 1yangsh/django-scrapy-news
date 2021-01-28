from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import NewsSerializer
from news.models import New

class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]