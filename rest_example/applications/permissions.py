from rest_framework.permissions import BasePermission
from rest_framework.authentication import get_authorization_header


class ApplicationAPIKeyPermission(BasePermission):
    message = 'Requests not allowed.'

    def has_permission(self, request, view):
    	auth = get_authorization_header(request).split()
    	print('auth', auth)
    	return True