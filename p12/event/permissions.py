from rest_framework.permissions import BasePermission
from .models import Event


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "manager":
            return True
        if request.user.role == 'sales':
            if view.action in ['create', 'list']:
                return True
            if view.action in ['retrieve', 'update']:
                event = Event.objects.filter(id=view.kwargs['pk'])
                if event[0]:
                    if event[0].sales_contact.id == request.user.id:
                        print('ok')
                        return True
        if request.user.role == 'support':
            if view.action == 'list':
                return True
            if view.action in ['retrieve', 'update']:
                event = Event.objects.filter(id=view.kwargs['pk'])
                if event[0]:
                    if event[0].support_contact:
                        if event[0].support_contact.id == request.user.id:
                            return True
        else:
            return False
