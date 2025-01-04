from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView,DetailView
from .models import Product
from django.views.generic.edit import CreateView, UpdateView,DeleteView
# Create your views here.

class TopView(TemplateView):
    template_name ='top.html'


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')


class ProductDetailView(DetailView):
    model = Product