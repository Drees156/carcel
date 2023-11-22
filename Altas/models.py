from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class Ppl(models.Model):
    nu = models.CharField(primary_key=True, max_length=10)
    apellidos_nombres = models.CharField(max_length=100)
    patio = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return "Nu: %s, Apellidos y Nombres: %s, Patio: %s" % (self.nu, self.apellidos_nombres, self.patio)