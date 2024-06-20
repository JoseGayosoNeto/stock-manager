from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import CategoriesForm
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories_create.html'
    form_class = CategoriesForm
    success_url = reverse_lazy('category-list')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories_detail.html'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories_update.html'
    form_class = CategoriesForm
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('category-list')
