from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import InflowForm
from .models import Inflow

class InflowListView(ListView):
    model = Inflow
    template_name = 'inflows_list.html'
    context_object_name = 'inflows'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        
        if product:
            queryset = queryset.filter(product__title__icontains=product)
            
        return queryset

class InflowCreateView(CreateView):
    model = Inflow
    template_name = 'inflows_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow-list')

class InflowDetailView(DetailView):
    model = Inflow
    template_name = 'inflows_detail.html'
