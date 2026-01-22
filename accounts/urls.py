from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    # path('cart/',views.cart,name='cart'),
    # path('add_cart/<int:product_id>/',views.add_cart, name='add_cart'),
    # path('remove_cart/<int:product_id>/<int:cart_item_id>/',views.remove_cart, name='remove_cart'),
    # path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',views.remove_cart_item, name='remove_cart_item'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]