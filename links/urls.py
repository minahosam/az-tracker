from django.urls import path
from .views import *
app_name='links'
urlpatterns = [
    path('',home,name='home'),
    path('delete/<pk>/',deleteLink.as_view(), name='delete'),
    path('update/',update,name='update'),
]
