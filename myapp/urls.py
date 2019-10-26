from django.urls import path,re_path
from myapp import views

app_name = "myapp"
urlpatterns=[
    path('',views.home,name='home'),
    path("register/",views.register,name="register"),
    path('user_login/',views.user_login,name='login'),
    path("logout/",views.user_logout,name='logout'),
    path('about_us/',views.about_us,name='about_us'),
    path('food_list/',views.food_list,name='food_list'),
    path('create/',views.FoodCreateView.as_view(),name='create'),
    re_path(r'^food/(?P<pk>\d+)/update/$',views.FoodUpdateView.as_view(),name="update_food"),
    re_path(r'^food/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name="food_remove"),
    re_path(r'^add_to_cart/(?P<pk>\d+)/$',views.cart,name="cart"),
    re_path(r'^your_cart/(?P<pk>\d+)/$',views.adding_to_cart,name="your_cart"),
    re_path(r'^your_cart/(?P<pk>\d+)/delete/$',views.clear_cart,name="your_cart_delete"),
    re_path(r'^your_cart/(?P<pk>\d+)/order/$',views.order_creating,name="your_cart_order"),
    re_path(r'^orders/$',views.your_orders,name="your_order"),
    re_path(r'^orders/(?P<pk>\d+)/$',views.change_status,name="change_status"),
    re_path(r'^cart/(?P<pk>\d+)/delete/$',views.cart_delete,name="cart_delete"),

]
