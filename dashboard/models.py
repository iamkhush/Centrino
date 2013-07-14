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