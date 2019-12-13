from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response

from rest_example.applications.models import Application
from rest_example.applications.serializers import ApplicationSerializer
from rest_example.applications.permissions import ApplicationAPIKeyPermission

from annoying.functions import get_object_or_None


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
        obj = get_object_or_404(Application, api_key=api_key)
        serializer = ApplicationSerializer(obj)
        return Response(serializer.data, status=HTTP_200_OK)


class ApplicationViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    """
    A viewset that provides `retrieve`, `create`, 'update' actions.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [ApplicationAPIKeyPermission]

    def get_object(self):
        api_key = self.request.META.get("HTTP_API_KEY", None)
        obj = get_object_or_404(Application, api_key=api_key)
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request):
        obj = self.get_object()
        serializer = ApplicationSerializer(obj)
        return Response(serializer.data, status=HTTP_200_OK)
