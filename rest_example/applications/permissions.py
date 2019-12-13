from rest_framework.permissions import BasePermission


class ApplicationAPIKeyPermission(BasePermission):
    message = "Requests not allowed."

    def has_permission(self, request, view):
    	# TODO: Implement checking permissions
        return True
