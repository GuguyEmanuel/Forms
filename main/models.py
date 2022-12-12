from django.db import models

# Create your models here.

SEX_LIST = [
  ('Masculino', 'Masculino'),
  ('Feminino', 'Feminino')
]

class MiniCurso(models.Model):
  nome = models.CharField(max_length=150)

  def __str__(self) -> str:
    return self.nome
  
class Curso(models.Model):
  nome = models.CharField(max_length=150)
  
  def __str__(self) -> str:
    return self.nome  

class Aluno(models.Model):
  nome = models.CharField(max_length=150)
  cpf = models.CharField(max_length=11)
  dataNascimento = models.DateTimeField()
  email = models.EmailField()
  endereco = models.CharField(max_length=150)
  sexo = models.CharField(max_length=150, choices=SEX_LIST, default='Feminino')
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  minicursos = models.ManyToManyField(MiniCurso)
  
  
  def __str__(self) -> str:
    return self.nome