from django.views.generic import ListView
from .models import Category, WorkInstance

class WorkInstanceListView(ListView):
    model = WorkInstance
    #template_name = 'your_model_list.html'
    #context_object_name = 'your_model_list'
