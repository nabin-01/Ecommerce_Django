from django.urls import path
from .views import *
app_name = 'myapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', ItemListView.as_view(),  name='category'),
    path('products/<slug>', ItemDetailView.as_view(), name='products'),
    path('contact/', contact, name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('account/', signup, name='account'),
    path('review/', review_item, name='review'),
    path('cart/<slug>', cart, name='cart'),
    path('my_cart/', CartView.as_view(), name='my_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('delete_single_cart/<slug>', delete_single_cart, name='delete_single_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('totals/', totals, name="totals"),
]
