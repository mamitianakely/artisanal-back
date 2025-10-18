from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<str:id_category>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]