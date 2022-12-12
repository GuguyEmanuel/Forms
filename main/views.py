from django.shortcuts import render
from .forms import AlunoForm

# Create your views here.

def inscricao(request):
  if request.method == 'POST':
    form = AlunoForm(request.POST) 
    if form.is_valid():
      form.save()
      form = AlunoForm()
  else:
    form = AlunoForm()

  form = AlunoForm()
  return render(request, 'inscricao.html', {'form' : form})