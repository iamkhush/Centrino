from django.db import models

class dashboard(models.Model):
	fielda = models.TextField(max_length=10)
	fieldb = models.IntegerField()
	fieldc = models.IntegerField()
	fieldd = models.IntegerField()
	fielde = models.IntegerField()
	fieldf = models.IntegerField()

class submitteddata(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()


class fleximodel(models.Model):
	name = models.TextField(null=True)
	age = models.IntegerField(null=True)
	email = models.TextField(null=True)
	temp_data = models.TextField(null=True)