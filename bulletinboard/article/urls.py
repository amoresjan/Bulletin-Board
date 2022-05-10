from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleDashboardView.as_view(), name='articleDashboard'),
    path('create/', views.articleRegistrationView.as_view() , name='articleRegistration')
]