import uuid

from django.db.models import (
	Model,
    CharField
)


class Application(Model):

	title = CharField(max_length=128)
	api_key = CharField(unique=True, max_length=36)

	@classmethod
	def api_key_exists(cls, api_key):
		return cls.objects.filter(api_key=api_key).exists()

	def generate_new_api_key(self):
		api_key = str(uuid.uuid4())
		return api_key.replace('-', '')

	def set_new_api_key(self):
		api_key = self.generate_new_api_key()
		while self.__class__.api_key_exists(api_key):
			api_key = self.generate_new_api_key()
		self.api_key = api_key

	def save(self, *args, **kwargs):
		if not self.id:
			self.set_new_api_key()
		super().save(*args, **kwargs)
