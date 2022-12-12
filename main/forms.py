from django import forms
from main.models import Aluno

class DatePickerInput(forms.DateInput):
  input_type = 'date'

class TimePickerInput(forms.TimeInput):
  input_type = 'time'

class AlunoForm(forms.ModelForm):
  class Meta:
    model=Aluno
    fields= '__all__'   
    labels= {
      'dataNascimento' : 'Data de nascimento',
      'cpf': 'CPF', 
      'endereco' : 'Endereço'
    }

    widgets = {
      'curso': forms.Select(attrs={'type': 'select'}),
      'minicursos': forms.CheckboxSelectMultiple(),
      'sexo': forms.RadioSelect(),
      'dataNascimento': forms.TimeInput(attrs={'type': 'date'}),
      
    }