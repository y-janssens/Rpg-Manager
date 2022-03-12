from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CharacterSheet


def loginUser(request):
    page_title = "Connexion"
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Le nom d\'utilisateur n\'existe pas')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            messages.error(
                request, 'Le nom d\'utilisateur et/ou le mot de passe sont incorrects')
    return render(request, 'fiches/login.html', {'page_title': page_title})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


@login_required(login_url='login')
def fiches(request):
    page_title = "Carrières Marbrume"
    fiches = CharacterSheet.objects.all()
    context = {'page_title': page_title, 'fiches': fiches}
    return render(request, 'fiches/list.html', context)


@login_required(login_url='login')
def fiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    page_title = f"Carrière {fiche.name}"
    context = {'page_title': page_title, 'fiche': fiche}
    return render(request, 'fiches/sheets.html', context)
