from rest_framework.permissions import BasePermission

class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff

class TeacherDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return request.user.is_staff


class StudentDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_staff

class StudyCenterPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff


class StudyCenterDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff