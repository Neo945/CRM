from django.urls import path

from accounts.views import get_user, login_view, logout_view, reg_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('get/', get_user, name='getuser'),
    path('register/', reg_view, name='register'),
    path('logout/', logout_view, name='register'),
]