from django.db import models
import os
from django.conf import settings
# Create your models here.

class Image(models.Model):
	name = models.CharField(max_length=30)
	desc = models.CharField(max_length=100)
	date = models.DateField()
	img = models.FileField(upload_to='catalog')

	def delete(self):
		os.remove(self.img.path)
		return super(Image, self).delete()


	def __str__(self):
		return self.id




