from django.urls import path, re_path
from pythonDev import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demand/', views.demand, name='demand'),
    path('geography/', views.geography, name='geography'),
    path('skills/', views.skills, name='skills'),
    path('latest/', views.latest, name='latest'),
]
