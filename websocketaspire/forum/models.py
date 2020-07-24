from django.db import models
from django.contrib.auth.models import User


class TimeStampModel(models.Model):

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Discussion(TimeStampModel):

	title = models.CharField(
		max_length=254,
		verbose_name='Discussion Title'
		)
	creator = models.ForeignKey(
		User,
		on_delete=models.CASCADE
		)

	class Meta:
		db_table = 'discussion'


class Post(TimeStampModel):
	discussion = models.ForeignKey(
		Discussion,
		on_delete=models.CASCADE, 
		related_name='posts'

		)
	content = models.TextField(
		max_length=1000,
		verbose_name='Post Content'
		)
	creator = models.ForeignKey(
		User,
		on_delete=models.CASCADE
		)

	class Meta:
		db_table = 'post'


