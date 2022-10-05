from datetime import datetime
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
import random

from AppCoder.models import Familiar

def crear_persona(request, nombre, apellido):

    edad=random.randrange(1,99) 

    persona= Familiar(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=datetime.now())
    persona.save()
    template=loader.get_template('crear_persona.html')
    template_renderizado= template.render({'personas': persona})

    return HttpResponse(template_renderizado)

    
def ver_persona(request):
    personas= Familiar.objects.all()
    template=loader.get_template('ver_persona.html')
    template_renderizado= template.render({'personas': personas})


    return HttpResponse(template_renderizado)