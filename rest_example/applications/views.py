from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_example.applications.models import Application
from rest_example.applications.serializers import ApplicationSerializer


class ApplicationViewSet(ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Application's.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
