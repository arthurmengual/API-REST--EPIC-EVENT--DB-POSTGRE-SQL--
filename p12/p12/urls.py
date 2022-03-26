from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from client.views import ClientViewset
from contract.views import ContractViewset
from event.views import EventViewset
from rest_framework import routers


router = routers.SimpleRouter()
router.register("client", ClientViewset)
router.register("contract", ContractViewset)
router.register("event", EventViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rest_framework.urls")),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
