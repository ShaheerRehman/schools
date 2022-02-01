from django.shortcuts import render
from django.views.generic import (View, 
                                  TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'
    # by making everything after models. lowercase and adding _list. 

    # Example of making your own:
    # context_object_name = 'schools'
    # normally we get the same list of objects by using models.objects.all()
    # context_object_name = 'schoollst'
    model = models.School # School class will be assigned to model
    # all objects of that class will go in school_list defined by the class attribute context_object_name
    
class SchoolDetailView(DetailView):
    
    context_object_name = 'schooldtl'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    
    
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location') #basically a security measure
    model = models.School
    
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
    # we use reverse_lazy with cbv while reverse with fbv. reverse returns a string while reverse lazy returns an object