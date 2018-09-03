from django.urls import path
from .views import home, my_logout, HomePageView, MyView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('home2/', HomePageView.as_view(), name='logout1'),
    path('view/', MyView.as_view(), name='view'),
]