from rest_framework.permissions import BasePermission
from .models import Contract


class ContractPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "manager":
            return True
        if request.user.role == 'sales':
            if view.action in ['create', 'list']:
                return True
            if view.action in ['retrieve', 'update']:
                contract = Contract.objects.filter(id=view.kwargs['pk'])
                if contract:
                    if contract[0].sales_contact.id == request.user.id:
                        return True
        else:
            return False
