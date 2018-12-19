from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,DetailView
from . import models

class IndexView(TemplateView):
    template_name='index.html'

class SchoolListVeiw(ListView):
    context_object_name='schools'
    model = models.School
    
class SchoolDetailView (DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='basic_app/school_detail.html'