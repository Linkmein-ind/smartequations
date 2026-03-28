from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('training/', views.training, name='training'),
    path('data_science/', views.data_science, name='data_science'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('cloud/', views.cloud, name='cloud'),
    path('internship/', views.internship, name='internship'),
    path('internship_details/', views.internship_details, name='internship_details'),
    path('request-call/', views.request_call, name='request_call'),
    path('enroll-internship/', views.enroll_internship, name='enroll_internship'),

]