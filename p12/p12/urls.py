from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
import client.views as clientviews
import contract.views as contractviews
import event.views as eventviews
from rest_framework import routers


router = routers.SimpleRouter()
router.register('client', clientviews.ClientViewset)
router.register('contract', contractviews.ContractViewset)
router.register('event', eventviews.EventViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
