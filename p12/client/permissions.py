from rest_framework.permissions import BasePermission
from event.models import Event


class ClientPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'manager':
            return True
        if request.user.role == 'sales':
            if view.action == 'create':
                return True
            elif view.action in ['retrieve', 'update']:
                if request.user.pk == obj.sales_contact.pk:
                    return True
                else:
                    False
            else:
                return False
        elif request.user.role == 'support':
            if view.action == 'retrieve':
                events = Event.objects.filter(support_contact=request.user)
                for event in events:
                    if event.client.pk == obj.pk:
                        return True
            else:
                return False
        else:
            return False
