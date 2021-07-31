from django.db import models

# Create your models here.
class MyCard(models.Model):
    name = models.CharField(max_length=200)
    date_and_time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="allimg")
    like = models.BooleanField(default=False)
