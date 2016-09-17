# -*- encoding: utf-8 -*-
from django.db import models

class presente(models.Model):

    nome = models.CharField(max_length=250, unique=True)
    descricao = models.TextField()
    comprado = models.BooleanField()
    img = models.ImageField(upload_to='fotopresente');
    link = models.CharField(max_length=350)

    def __str__(self):
        return self.nome.encode('utf8')

    def publish(self):
            self.save()

class Convidado(models.Model):

    nome = models.CharField(max_length=250, unique=True)
    presenca = models.BooleanField()
    npessoas = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        vai = ""
        if self.presenca is not None:
            if self.presenca:
                vai = " - Vai".encode('utf-8')
            else:
                vai = " - Nao Vai".encode('utf-8')

        return self.nome.encode('utf-8') + vai.encode('utf-8')
