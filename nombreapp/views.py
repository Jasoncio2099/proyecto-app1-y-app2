from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html="""
    <h1>soy el index de la app1</h1>
    <h2>Hola!<h2>
    """
    return HttpResponse(html)   

def pagina1(request):
    html="""
    <h1>pagina pulenta</h1>
    <h2> hola pagina <h2>
    """
    return HttpResponse(html)
# Create your views here.
