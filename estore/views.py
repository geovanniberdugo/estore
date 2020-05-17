from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {
        'message': 'Listado de Productos',
        'title': 'Productos',
        'products': [
            {'title':'Playera', 'price':'5', 'stock':True},
            {'title':'Camisa', 'price':'50', 'stock':True},
            {'title':'Mochila', 'price':'20', 'stock':False}
        ]
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username') #POST is a dictionary
        password = request.POST.get('password') #If key doesnt exists, get method returns a None value
        print(username, password)
    return render(request, 'users/login.html', {})