from rest_framework import permissions
from rolepermissions.checkers import has_permission

class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (view.action in ['update', 'partial_update', 'destroy', 'list', 'create']
                and has_permission(request.user,'modify_courses_subjects_tags'))

