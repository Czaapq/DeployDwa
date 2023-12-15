from django.db import models

# Create your models here.

class Bibik(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    pseudonim = models.CharField(max_length=15, null=True, blank=True)
    ocena1na10 = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True)
    opis = models.TextField(default="")

    def __str__(self):
        return self.imie_pseudonim()

    def imie_pseudonim(self):
        return "{} {}".format(self.imie, self.pseudonim)
