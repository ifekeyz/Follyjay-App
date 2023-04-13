from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('beauty_health/',views.beauty_health_page, name='beauty_health_page'),
    path('beauty_health/item<int:beauty_id>',views.beauty, name='beauty'),
    path('confectioneries/',views.confectioneries_page, name='confectioneries'),
    path('confectioneries/item<int:confectionerie_id>',views.confectionerie, name='confectionerie'),
    path('drinks/',views.drinks_page, name='drinks_page'),
    path('drinks/item<int:drink_id>',views.drink, name='drink'),
    path('grain_flour/',views.grain_flour_page, name='grain_flour_page'),
    path('grain_flour/item<int:grain_id>',views.grain, name='grain'),
    path('meat_vegetable/',views.meat_vegetable_page, name='meat_vegetable_page'),
    path('meat_vegetable/item<int:meat_id>',views.meat, name='meat'),
    path('species_oil/',views.species_oil_page, name='species_oil_page'),
    path('species_oil/item<int:oil_id>',views.oil, name='oil'),
    path('tuber/',views.tuber_page, name='tuber_page'),
    path('tubers/item<int:tuber_id>',views.tuber, name='tuber'),
    path('untensils/',views.untensils_page, name='untensils_page'),
    path('untensils/item<int:africa_id>',views.africa, name='africa'),
    path('register_login/', views.register_login, name='register_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
    path('updatecart',views.updateCart, name="updatecart"),
    path('updatequantity',views.updateQuantity, name="updatequantity"),
]