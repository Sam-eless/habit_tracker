from rest_framework.permissions import BasePermission


class OwnerOrStuff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Moderators').exists()

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        elif request.user.is_staff or request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Moderators').exists()
