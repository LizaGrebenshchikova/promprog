
from __future__ import unicode_literals

from django.db import models

from datetime import datetime
# Create your models here.
class ToDoList(models.Model):
	"""docstring for ToDoList"""
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title
	text = models.TextField()
	date_creation = models.DateTimeField(default=datetime.now)

		