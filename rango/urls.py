from django.urls import path
from rango import views

app_name ='rango'

urlpatterns=[
    path('', views.index, name='index'),
]


app_name ='about'
urlpatterns=[
    path('', views.about, name='about'),
]