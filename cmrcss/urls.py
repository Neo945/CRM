from django.urls import path

from cmrcss.views import index

app_name = 'cmrcss'

urlpatterns = [
    path('feedback/<str:token>', index, name='index'),
]