# forms.py
from django import forms


class NewsSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Keyword')
    

class GetNewsForm(forms.Form):
    pass