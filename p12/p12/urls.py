from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('client', views.ClientViewset)
router.register('contract', views.ContractViewset)
router.register('event', views.EventViewset)
router.register('event-status', views.EventStatusViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
