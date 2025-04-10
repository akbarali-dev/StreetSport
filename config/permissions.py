from rest_framework.permissions import BasePermission

class IsOwnerUser(BasePermission):
    def has_permission(self, request, view):
        # print(request.user.is_authenticated and request.user.role == 'owner')
        print(request.user.role)
        # print(request.user.is_authenticated)
        return request.user.is_authenticated and request.user.role == 'owner'

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        return request.user.is_authenticated and request.user.role == 'admin'

class IsUser(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        return request.user.is_authenticated and request.user.role == 'user'
