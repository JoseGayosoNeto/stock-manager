from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import SupplierForm
from .models import Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
            
        return queryset

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'suppliers_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier-list')

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers_detail.html'

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'suppliers_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier-list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('supplier-list')
