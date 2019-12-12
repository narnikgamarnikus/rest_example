import pytest

pytestmark = pytest.mark.django_db


class TestApplicationModel:
    
    def test_generate_new_api_key(self, application):
        assert len(application.api_key) == 32

    def test_api_key_exists(self, application):
        assert application.api_key_exists(api_key_exists.api_key)