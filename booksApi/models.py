from django.db import models

# Create your models here.

class Books(models.Model):
	name=models.CharField(max_length=200)
	rating=models.IntegerField()
	is_published = models.BooleanField(default=True)

	def __str__(self):
		return self.name	