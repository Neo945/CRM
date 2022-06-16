
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/accounts/',include('accounts.urls',namespace='accounts')),
    path('api/v1/leads/',include('leads.urls',namespace='leads')),
    path('api/v1/customer/',include('customer.urls',namespace='customer')),
    path('api/v1/cmrcss/',include('cmrcss.urls',namespace='cmrcss')),
    path('', include('pages.urls', namespace='pages')),
]
