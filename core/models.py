from django.db import models

class Apoiadores (models.Model):
    cidades = (
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro')
    )
    nome = models.CharField(max_length=50)
    nascimento = models.DateField()
    email = models.EmailField(primary_key=True)
    img_perfil = models.ImageField(upload_to="static/media/profile/", null=True)
    profissao = models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)
    cidade = models.CharField(max_length=5, choices=cidades, blank=True)
    linkdin = models.URLField()
    github = models.URLField()

