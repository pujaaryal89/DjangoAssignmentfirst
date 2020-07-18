from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    mobile = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
	title=models.CharField(max_length=100)
	author=models.ForeignKey(Author,on_delete=models.CASCADE)
	description=models.TextField()
	image=models.ImageField(upload_to="blog")
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __self__(self):
		return self.title