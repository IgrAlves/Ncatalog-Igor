from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Roupa(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="imagens/")
    descript = models.TextField()

class Curtida(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothing = models.ForeignKey(Roupa, on_delete=models.CASCADE)

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothe = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    content = models.TextField()