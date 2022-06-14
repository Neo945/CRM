
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/',include('accounts.urls',namespace='accounts')),
    path('api/v1/leads/',include('leads.urls',namespace='leads')),
    path('api/v1/customer/',include('customer.urls',namespace='customer')),
    path('api/v1/cmrcss/',include('cmrcss.urls',namespace='cmrcss')),
    path('', include('pages.urls', namespace='pages')),
]
