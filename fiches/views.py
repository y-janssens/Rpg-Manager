from django.shortcuts import render, redirect
from decorators import login_required
from .models import *
from carrieres.models import *
from reputations.models import *
from .forms import *
from reputations.forms import *
from competences.models import *
from competences.forms import *
from .utils import searchFiche, paginateFiche
from reputations.text import flavorText


@login_required(login_url='login')
def fiches(request):
    page_title = "Carrières Marbrume"
    carrieres = Carriere.objects.all()
    form = CharacterSheetForm()
    fiches, search_query = searchFiche(request)
    custom_range, fiches = paginateFiche(request, fiches, 15)
    url = f"{request.scheme}://{request.META['HTTP_HOST']}/fiche/details/"
    context = {'page_title': page_title, 'fiches': fiches, 'carrieres': carrieres,
               'form': form, 'search_query': search_query, 'custom_range': custom_range, 'url': url}
    return render(request, 'fiches/fiches.html', context)


@login_required(login_url='login')
def fiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    form = CharacterSheetForm(instance=fiche)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)
    repForm = CommonReputationForm(instance=reputation)
    skills = Skill.objects.all()
    sheets = SkillSheet.objects.filter(owner_id=pk)
    sheetForms = []
    index = 0

    for skill in sheets:
        sheetForm = SkillSheetForm(instance=sheets[index])
        setattr(sheetForm, 'id', skill.id)
        setattr(sheetForm, 'name', skill.skill)
        sheetForms.append(sheetForm)
        index += 1

    page_title = f"Carrière {fiche.name}"
    url = f"{request.scheme}://{request.META['HTTP_HOST']}/fiche/details/"
    rurl = f"{request.scheme}://{request.META['HTTP_HOST']}/reputations/details/"

    context = {'page_title': page_title,
               'fiche': fiche, 'form': form, 'skills': skills, 'sheetForms': sheetForms, 'repForm': repForm, 'carriere': carriere, 'reputation': reputation, 'flavorText': flavorText, 'url': url, 'rurl': rurl}
    return render(request, 'fiches/fiche_details.html', context)


@login_required(login_url='login')
def editFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)

    if request.method == "POST":
        form = CharacterSheetForm(request.POST, instance=fiche)

        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


def ficheDetails(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)

    page_title = f"Carrière {fiche.name}"
    proxy = f"{request.scheme}://{request.META['HTTP_HOST']}"
    context = {'page_title': page_title, 'fiche': fiche,
               'carriere': carriere, 'proxy': proxy}
    return render(request, 'fiches/iframe.html', context)


def ficheModel(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)

    sheets = SkillSheet.objects.filter(owner_id=pk)

    competences = []
    index = 0

    for skill in sheets:
        sheetItem = sheets[index]
        setattr(sheetItem, 'id', skill.id)
        setattr(sheetItem, 'name', skill.skill)
        competences.append(sheetItem)
        index += 1

    page_title = f"Carrière {fiche.name}"
    proxy = f"{request.scheme}://{request.META['HTTP_HOST']}"
    context = {'page_title': page_title, 'fiche': fiche, 'carriere': carriere,
               'reputation': reputation, 'competences': competences, 'flavorText': flavorText, 'proxy': proxy}
    return render(request, 'fiches/modele.html', context)


def ficheModelIframe(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)

    sheets = SkillSheet.objects.filter(owner_id=pk)

    competences = []
    index = 0

    for skill in sheets:
        sheetItem = sheets[index]
        setattr(sheetItem, 'id', skill.id)
        setattr(sheetItem, 'name', skill.skill)
        competences.append(sheetItem)
        index += 1

    page_title = f"Carrière {fiche.name}"
    proxy = f"{request.scheme}://{request.META['HTTP_HOST']}"
    context = {'page_title': page_title, 'fiche': fiche, 'carriere': carriere,
               'reputation': reputation, 'competences': competences, 'flavorText': flavorText, 'proxy': proxy}
    return render(request, 'fiches/modele_iframe.html', context)


@login_required(login_url='login')
def addFiche(request):
    form = CharacterSheetForm()

    if request.method == "POST":
        form = CharacterSheetForm(request.POST)

        if form.is_valid():
            fiche = form.save(commit=False)
            fiche.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect('/')


@login_required(login_url='login')
def delFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    fiche.delete()
    return redirect('/')


@login_required(login_url='login')
def confirmFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "fiche"

    context = {'page_title': page_title, 'fiche': fiche, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def links(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)
    sheets = SkillSheet.objects.filter(owner_id=pk)

    page_title = f"{fiche.name} : Liens utiles"
    url = f"{request.scheme}://{request.META['HTTP_HOST']}/fiche/details/"
    rurl = f"{request.scheme}://{request.META['HTTP_HOST']}/reputations/details/"
    curl = f"{request.scheme}://{request.META['HTTP_HOST']}/competences/details/"
    murl = f"{request.scheme}://{request.META['HTTP_HOST']}/fiche/model/iframe/"

    context = {'page_title': page_title, 'fiche': fiche, 'carriere': carriere,
               'reputation': reputation, 'sheets': sheets, 'url': url, 'rurl': rurl, 'murl': murl, 'curl': curl}
    return render(request, 'fiches/links.html', context)
