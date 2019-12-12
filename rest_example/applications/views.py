from rest_framework.viewsets import GenericViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_example.applications.models import Application
from rest_example.applications.serializers import ApplicationSerializer
from rest_example.applications.permissions import ApplicationAPIKeyPermission

from annoying.functions import get_object_or_None


class ApplicationViewSet(GenericViewSet):
    """
    A simple ViewSet for viewing Application's.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [ApplicationAPIKeyPermission]

    @action(detail=False, methods=["get"])
    def test(self, request):
        api_key = request.query_params.get("api_key", None)
        instance = get_object_or_None(Application, api_key=api_key)
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({"message": "Not found"}, status=HTTP_404_NOT_FOUND)
