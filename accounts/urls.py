from django.urls import path

from accounts.views import get_user, login_view, logout_view, reg_view, send_email_data, update_password

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('get/', get_user, name='getuser'),
    path('register/', reg_view, name='register'),
    path('logout/', logout_view, name='register'),
    path('send/email/', send_email_data, name='send_emai'),
    path('update/password/', update_password, name='update_password'),
]