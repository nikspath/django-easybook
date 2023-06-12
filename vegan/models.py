from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Receipe(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name=models.CharField(max_length=20)
	description=models.TextField()
	image=models.FileField(default="",upload_to='receipe')
	receipe_view_count=models.IntegerField(default=1)

	def __str__(self):
		return self.name