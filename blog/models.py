from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog/images",default=" ")
    content = models.TextField()
    category = models.CharField(max_length=200,default="actress")
    slug = models.CharField(max_length=130,default="")
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return(f"title by  {self.title}")
    