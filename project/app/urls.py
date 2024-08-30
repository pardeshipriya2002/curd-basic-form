
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path("login/",views.login,name='login'),
    
    path("query/",views.query,name='query'),
    path("delete/<int:pk>",views.delete,name='delete'),
]
