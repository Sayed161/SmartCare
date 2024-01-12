from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="service/image/")
    class Meta:
        verbose_name_plural = "Service"