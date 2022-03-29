from rest_framework.permissions import BasePermission
from .models import Client


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "manager":
            return True
        if request.user.role == 'sales':
            if view.action in ['create', 'list']:
                return True
            if view.action in ['retrieve', 'update']:
                client = Client.objects.filter(id=view.kwargs['pk'])
                if client:
                    if client[0].sales_contact.id == request.user.id:
                        return True
        if request.user.role == 'support':
            if view.action in ['list', 'retrieve']:
                return True
        return False
