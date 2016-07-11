from __future__ import unicode_literals
from datetime import datetime, time
#uses pre-built user from django authorization
from django.contrib.auth.models import User

from django.db import models

class Comment(models.Model):
	comment = models.TextField()
#sets date time to the current time
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	comment_creator = models.ForeignKey(User)


