from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Curso

# Create your views here.

def crear_curso(request):
    curso = Curso(nombre='Prueba2', camada=5)
    curso.save()
    
    return HttpResponse(f'{curso.nombre} {curso.camada}')

def ver_curso(request):
    cursos = Curso.objects.all()
    
    texto = ''
    
    for curso in cursos:
        texto += f'Curso: {curso.nombre} <br>'
    
    return HttpResponse(f'{texto}')

def prueba_templates(request):
    
    # una forma de cargar el template
    # template = loader.get_template('AppCoder/index.html')
    # documento = template.render({})
    # return HttpResponse(documento)
    
    # otra forma
    return render(request , 'AppCoder/index.html', {})