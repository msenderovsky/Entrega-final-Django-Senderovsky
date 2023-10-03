from django.http import HttpResponse
from django.template import Template, Context, loader
def asd(req):
    return ()

def probando_template(req):

    plantilla=loader.get_template('template1.html')
    documento= plantilla.render()
    return HttpResponse(documento)

def origen(req,nombre):
    documentoDeTexto=f'mi nombre es: {nombre}'
    return HttpResponse(documentoDeTexto)