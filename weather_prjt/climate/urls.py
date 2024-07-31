from django.urls import path

from climate import views

urlpatterns = [

    path('',views.index,name='index'),
]