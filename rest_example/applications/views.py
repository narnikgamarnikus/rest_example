from rest_framework.mixins import GenericViewSet
from rest_framework.decorators import action
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response

from rest_example.applications.models import Application
from rest_example.applications.serializers import ApplicationSerializer
from rest_example.applications.permissions import ApplicationAPIKeyPermission


class ApplicationViewSet(GenericViewSet):
    """
    A simple ViewSet for viewing Application's.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [ApplicationAPIKeyPermission]

    @action(detail=False, methods=['get'])
    def test(self, request, pk=None):
    	authorization_header = get_authorization_header(request).split()
    	return Response({})



