from django.urls import path
from . import views
from .views import AddProductView, UpdateProductView, DeleteProductView

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
    path('/create/', AddProductView.as_view(), name='create'),
    path('update/<slug:pk>/', UpdateProductView.as_view(), name='update'),
    path('/<slug:pk>/delete', DeleteProductView.as_view(), name='delete'),
]