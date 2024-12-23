from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product
from django.views.generic.edit import CreateView
# Create your views here.

class TopView(TemplateView):
    template_name ='top.html'


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'