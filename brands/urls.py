from django.urls import path
from .views import BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView, BrandDeleteView


urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brand-list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('brands/<int:pk>/detail/', BrandDetailView.as_view(), name='brand-detail'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),
]
