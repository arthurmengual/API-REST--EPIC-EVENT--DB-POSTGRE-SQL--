from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.SimpleRouter()
router.register('client', views.ClientViewset)
router.register('user', views.UserViewSet)
router.register('contract', views.ContractViewset)
router.register('event', views.EventViewset)
router.register('event-status', views.EventStatusViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
