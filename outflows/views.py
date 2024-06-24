from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import OutflowForm
from .models import Outflow


class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflows_list.html'
    context_object_name = 'outflows'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        
        return queryset

class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflows_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow-list')

class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflows_detail.html'
