from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_example.applications.models import Application
from rest_example.applications.serializers import ApplicationSerializer
from rest_example.applications.permissions import ApplicationAPIKeyPermission

from annoying.functions import get_object_or_None

from rest_framework.views import APIView
from rest_framework.response import Response


class TestApplicationView(APIView):
    """
    View to testing applications app response.

    * Requires api_key authentication.
    * Only authorized users are able to access this view.
    """
    permission_classes = [ApplicationAPIKeyPermission]

    def get(self, request, format=None):
        """
        Return application by api_key in HEADERS.
        """
        api_key = request.META.get("HTTP_API_KEY", None)
        instance = get_object_or_None(Application, api_key=api_key)
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({"message": "Application not found"}, status=HTTP_404_NOT_FOUND)


class ApplicationViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing Application's.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [ApplicationAPIKeyPermission]
