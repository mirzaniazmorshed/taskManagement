from django.db import models
import datetime
from category.models import Category
# Create your models here.
class Task(models.Model):
    date = models.DateField(default=datetime.date.today)

    description = models.TextField()

    category = models.ManyToManyField(Category)
    
    is_completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.date