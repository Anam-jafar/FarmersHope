from django.urls import path
from . import views
from .views import ProductCreateView

urlpatterns = [
    path('', views.store, name="store"),
    path('add_product/', ProductCreateView.as_view(), name="add_product"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]