from django.db import models

class store(models.Model):
	bookimage=models.ImageField(upload_to="Books",blank=True,null=True)
	bookname=models.CharField(max_length=50)
	releasedate=models.DateField(auto_now=False,auto_now_add=False)
	about=models.CharField(max_length=1000)

	def __str__(self):
		return self.bookname