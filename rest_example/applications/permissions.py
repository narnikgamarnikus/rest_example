from rest_framework.permissions import BasePermission

from rest_example.applications.models import Application

from annoying.functions import get_object_or_None


class ApplicationAPIKeyPermission(BasePermission):
    message = "Requests not allowed."

    def has_permission(self, request):
    	api_key = request.META.get('HTTP_API_KEY', None)
        return bool(get_object_or_None(Application, api_key=api_key))
