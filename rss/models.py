from django.db import models

# Create your models here.
class Rss(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    categoria = models.CharField(max_length=200)
    fuente = models.CharField(max_length=200)

    class Meta:
        db_table = 'rss_fuentes'