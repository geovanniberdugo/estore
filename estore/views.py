from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User

from products.models import Product

from .forms import RegisterForm

def index(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'message': 'Listado de Productos',
        'title': 'Productos',
        'products': products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)

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

def logout_view(request):
    logout(request)
    messages.success(request, 'Successful Exit')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect(index)

    form = RegisterForm(request.POST or None) #If method is POST then form is initialized 

    if request.method == 'POST' and form.is_valid(): #is_valid() call all clean_field and clean methods to validate field
        user = form.save() #In form.save() method create_user encrypts password
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect(index)


    return render(request, 'users/register.html', {'form':form})