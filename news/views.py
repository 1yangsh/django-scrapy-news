from django.views.generic import ListView, DetailView

from django.shortcuts import render
from news.models import New

# Search 기능 추가 
from news.forms import NewsSearchForm
from django.views.generic.edit import FormView
from django.db.models import Q





# Create your views here.
class NewsLV(ListView):
    model = New
    template_name = "news/news_all.html"
    context_object_name = "news" 

    paginate_by = 10


class NewsDV(DetailView):
    model = New


class SearchFormView(FormView):
    form_class = NewsSearchForm # forms.py에 생성
    template_name = "news/news_search.html"

    def form_valid(self, form):
        schword = self.request.POST['search_word']
        news_list = New.objects.filter(Q(title__icontains=schword) | Q(writer__icontains=schword) | Q(preview__icontains=schword)).distinct()

        # 검색된 결과 
        context = {}
       
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = news_list

        return render(self.request, self.template_name, context)