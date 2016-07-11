from __future__ import unicode_literals
from datetime import datetime, time
#uses pre-built user from django authorization
from django.contrib.auth.models import User
from django.db import models

#import messages and comments
from django.apps import apps
Comment = apps.get_app_config('comments').models['comment']
Message = apps.get_app_config('posts').models['message']

class Wall(models.Model):
	user = models.OneToOneField(User)

class Wall_User(models.Model):
	user = models.OneToOneField(User)
	#USER has email, password(hashed)required, username/required, first name, last name
	DOB = models.DateField()

#this is an extension of a class so input Comment as parameter
class Wall_Comment(Comment):
	message_id= models.ForeignKey(Message)

#create a class where a user can view and post on OTHER users' walls

class Wall_Message(Message):
	wall = models.ForeignKey(Wall)


