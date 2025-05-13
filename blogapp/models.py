from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="blogapp/images", default='')

    def __str__(self):
        return self.title


