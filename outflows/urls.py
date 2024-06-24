from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView


urlpatterns = [
    path('outflows/list/', OutflowListView.as_view(), name='outflow-list'),
    path('outflows/create/', OutflowCreateView.as_view(), name='outflow-create'),
    path('outflows/<int:pk>/details/', OutflowDetailView.as_view(), name='outflow-detail'),
]

