from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Item

# Create your views here.
class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name) 



class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        return render(request, self.template_name)
    
class ItemListView(ListView):
    template_name = 'shop.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()