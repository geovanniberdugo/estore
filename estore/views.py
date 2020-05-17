from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #POST is a dictionary
        password = request.POST.get('password') #If key doesnt exists, get method returns a None value
        user = authenticate(username=username, password=password) #returns None if user doesnt exists
        if user:
            login(request, user)
            messages.success(request, 'Welcome {} !!!'.format(user.username))
            return redirect(index)
        else:
            messages.error(request, 'Invalid user or password')

    return render(request, 'users/login.html', {'title':'Ecommerce Site'})