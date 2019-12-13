from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from rest_example.applications.models import Application


class ApplicationAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get("HTTP_API_KEY", None)
        if not api_key:
            return None

        try:
            application = Application.objects.get(api_key=api_key)
        except Application.DoesNotExist:
            raise AuthenticationFailed(
                "No such application"
            )  # raise exception if user does not exist

        return (application, None)
