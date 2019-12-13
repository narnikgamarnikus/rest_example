import pytest

pytestmark = pytest.mark.django_db


class TestApplicationModel:
    def test_generate_new_api_key(self, application):
        assert len(application.api_key) == 32

    def test_api_key_exists(self, application):
        assert application.__class__.api_key_exists(application.api_key)

    def test_set_api_key(self, application):
        old_api_key = application.api_key
        application.set_new_api_key()
        assert old_api_key != application.api_key
