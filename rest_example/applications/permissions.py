from rest_framework.permissions import BasePermission

from rest_example.applications.models import Application


class ApplicationAPIKeyPermission(BasePermission):

    message = "Requests not allowed."

    def has_permission(self, request, view):
        api_key = request.META.get("HTTP_API_KEY", None)
        if request.method == "POST":
            return True
        return Application.objects.filter(api_key=api_key).exists()
