from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SinlgeMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]