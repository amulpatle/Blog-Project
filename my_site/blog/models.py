from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now = True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
     