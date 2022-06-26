from django.urls import path
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('salespage/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('data/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('navlead/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('register/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='index.html'), name='home'),
]