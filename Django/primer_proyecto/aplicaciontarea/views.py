from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Marcador de posicion pra mostrar mas tarde una lista de todos los blogs")

def root(request):
    return redirect("blogs/")

def new(request):
    return HttpResponse('crear formulario de blog')

def create(request):
    return redirect('/')

def show(request, _numero, _nn):
    return HttpResponse(f'numero del blog {_numero},{_nn}')

def edit(request, _numero):
    return HttpResponse(f'Marcador de posicion para editar el blog {_numero}')

def delete(request, _numero):
    return redirect('/blogs')
