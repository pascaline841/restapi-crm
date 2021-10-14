from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            User.objects.get(username=request.user, role="ADMIN")
        except User.DoesNotExist:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        try:
            User.objects.get(username=request.user, role="ADMIN")
        except User.DoesNotExist:
            return False
        return True


class IsSaler(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "SALE":
            return request.method in ["POST", "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.role == "SALE":
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSalesContact(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "SALE":
            return request.method in ["POST", "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact:
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSupportContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.support_contact:
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS
