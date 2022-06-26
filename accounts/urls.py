from django.urls import path

from .views import create_jobs, get_company, get_jobs, get_user, login_view, logout_view, reg_view, send_email_data, update_password,create_company

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('get/', get_user, name='getuser'),
    path('register/', reg_view, name='register'),
    path('logout/', logout_view, name='register'),
    path('send/email/', send_email_data, name='send_emai'),
    path('update/password/', update_password, name='update_password'),
    path('create/company/', create_company, name='create_company'),
    path('company/<int:company_id>', get_company, name='create_job'),
    path('create/job/', create_jobs, name='create_job'),
    path('job/<int:job_id>', get_jobs, name='get_jobs'),
]