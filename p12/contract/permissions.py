from rest_framework.permissions import BasePermission


class ContractPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == "manager":
            return True
        if request.user.role == "sales":
            if view.action == "create":
                # vérifier si les sales peuvent créer des contrats et pour qui
                return True
            elif view.action in ["retrieve", "update"]:
                if request.user.pk == obj.sales_contact.pk:
                    return True
                else:
                    False
            else:
                return False
        else:
            return False
