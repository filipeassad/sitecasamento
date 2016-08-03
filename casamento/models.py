from django.db import models

class presente(models.Model):

    nome = models.CharField(max_length=250, unique=True)
    descricao = models.TextField()
    comprado = models.BooleanField()
    img = models.ImageField(upload_to='fotopresente');
    link = models.CharField(max_length=350)

    def __str__(self):
        return self.nome

    def publish(self):
            self.save()
