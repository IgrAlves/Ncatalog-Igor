from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'abc/index.html',{"card": Roupa.objects.all()})

def create(request):
    form = RoupaForm
    if request.method == "POST":
        form = RoupaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrado com sucesso!')
            return redirect('index')
        
    return render(request, "abc/adicionar.html", {"forms":form})

def edit(request, id):
    produto = Roupa.objects.get(pk=id)
    form = RoupaForm(instance=produto)
    return render(request, "abc/update.html",{"form":form, "produto":produto})


def update(request, id):
    try:
        if request.method == "POST":
            produto = Roupa.objects.get(pk=id)
            form = RoupaForm(request.POST, request.FILES, instance=produto)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    produto = Roupa.objects.get(pk=id)
    return render(request, "abc/read.html", {"produto":produto})

def delete(request, id):
    produto = Roupa.objects.get(pk=id)
    produto.delete()
    messages.success(request, 'item foi deletado com sucesso!')
    return redirect('index')

def listar(request):
    return render(request, 'abc/listar.html',{"cards": Roupa.objects.all()})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index") 
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'abc/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'abc/signup.html', {'form': form})

