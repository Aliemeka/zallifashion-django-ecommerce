from django.urls import path
from .views import HomeView, CartView, ItemListView

urlpatterns = [
    #home page url
    path('', HomeView.as_view(), name='home'),
    #shopping cart /cart/
    path('cart/', CartView.as_view(), name='shopping-cart'),
    #shop page /shop/
    path('shop/', ItemListView.as_view(), name='shop'),
]