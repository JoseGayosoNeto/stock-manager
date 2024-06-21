from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierDetailView, SupplierUpdateView, SupplierDeleteView


urlpatterns = [
    path('suppliers/list/', SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/<int:pk>/update', SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete')
]

