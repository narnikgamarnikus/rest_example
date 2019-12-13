from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from rest_example.applications.models import Application
from rest_example.applications.serializers import ApplicationSerializer
from rest_example.applications.permissions import ApplicationAPIKeyPermission

from annoying.functions import get_object_or_None


class ApplicationViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing Application's.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [ApplicationAPIKeyPermission]

