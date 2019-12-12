import pytest

pytestmark = pytest.mark.django_db


class TestApplicationModel:
    def test_generate_new_api_key(self, application):
        assert len(application.api_key) == 36
