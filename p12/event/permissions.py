from curses import flash
from distutils.log import error
from rest_framework.permissions import BasePermission


class EventPermission(BasePermission):

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
        if request.user.role == 'support':
            if view.action in ['retrieve', 'update']:
                if obj.support_contact:
                    if obj.support_contact.pk == request.user.pk:
                        return True
                    else:
                        return False
                else:
                    print('no support contact for this event')
                    # manage with exception
                    return False
            else:
                return False
        else:
            return False
