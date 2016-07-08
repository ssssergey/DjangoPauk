# -*- coding: utf-8 -*-

from models import SearchTerm
from django import forms


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchTerm
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        default_text = u'Поиск'
        self.fields['q'].widget.attrs['value'] = default_text
        self.fields['q'].widget.attrs['class'] = 'form-control'
        self.fields['q'].widget.attrs['onfocus'] = "if (this.value=='" + default_text + "')this.value = ''"

    include = ('q',)
