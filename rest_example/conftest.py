import pytest
from django.conf import settings
from django.test import RequestFactory

from rest_example.users.tests.factories import UserFactory

from rest_example.applications.tests.factories import ApplicationFactory
from rest_example.applications.models import Application


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()

@pytest.fixture
def application() -> Application:
    return ApplicationFactory()

@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
