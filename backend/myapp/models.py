from django.db import models

# Create your models here.
class Ficha(models.Model):
    # atributos base
    name = models.CharField(max_length=50)
    profissao = models.CharField(max_length=50)
    vida = models.IntegerField(default=0)
    forca = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    agilidade = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabedoria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)
    labia = models.IntegerField(default=0)
    percepcao = models.IntegerField(default=0)
    intuicao = models.IntegerField(default=0)
    fe = models.IntegerField(default=0)

    #status especias
    status_especiais = models.TextField(blank=True, null=True)

    #status religioso
    status_religiosos = models.TextField(blank=True, null=True)
        
    #religiao
    religiao = [
        ("Hibirismo", "Hibirismo"),
        ("Ateismo", "Ateismo"),
        ("Agnosticismo", "Agnosticismo"),
        ("Flowdiesto", "Flowdiesto"),
        ("Zudelista", "Zudelista"),
        ("Sanhismo", "Sanhismo"),
        ("Cristianismo", "Cristianismo")
    ]