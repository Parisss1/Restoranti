# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Kategorite(models.Model):
    emri = models.CharField(max_length=20)

    def __str__(self):
        return self.emri

class Produkte(models.Model):
    emri = models.CharField(max_length=50)
    pershkrimi = models.CharField(max_length=500)
    cmimi = models.IntegerField()
    foto = models.CharField(max_length=500)
    kategori = models.ForeignKey(Kategorite, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.emri

class AddToCart(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_product = models.ForeignKey(Produkte, on_delete = models.DO_NOTHING)
    quantity = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    orderd = models.BooleanField(default=False)

    @property
    def cmimi_total(self):
        return self.quantity * self.id_product.cmimi

    def __str__(self):
        return self.id_product.emri

class Commentsection(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    comment = models.TextField()

    def __str__(self):
        return self.user.username