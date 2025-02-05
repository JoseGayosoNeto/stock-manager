from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import OutflowForm
from .models import Outflow
from core.metrics import stock_metrics


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = stock_metrics.get_sales_metrics()
        
        return context

class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflows_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow-list')
    
    def form_valid(self, form):
        product = form.cleaned_data.get('product')
        
        form.instance.cost_price = product.cost_price
        form.instance.selling_price = product.selling_price
        
        return super().form_valid(form)

class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflows_detail.html'
