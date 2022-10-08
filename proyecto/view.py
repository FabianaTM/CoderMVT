from datetime import datetime
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
import random

from AppCoder.models import Familiar

def crear_persona(request):

    edad=random.randrange(1,99) 

    persona1= Familiar(nombre='Paola', apellido='Arena', edad=edad, fecha_nacimiento=datetime.now())
    persona2=Familiar(nombre='Fabiana', apellido='Torres Meza', edad=edad, fecha_nacimiento=datetime.now())
    persona3= Familiar(nombre='Ricardo', apellido='Fort', edad=edad, fecha_nacimiento=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()
    template=loader.get_template('crear_persona.html')
    template_renderizado= template.render({})

    return HttpResponse(template_renderizado)

    
def ver_persona(request):
    personas= Familiar.objects.all()
    template=loader.get_template('ver_persona.html')
    template_renderizado= template.render({'personas': personas})


    return HttpResponse(template_renderizado)