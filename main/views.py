from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

## Create your views here.




class ProizvodjacPlastikaList(ListView):
    template_name = 'main/plastika_by_proizvodjac.html'

    def get_queryset(self):
        self.proizvodjac = get_object_or_404(Proizvodjac, name=self.kwargs['proizvodjac'])
        return Proizvodjac.objects.filter(name=self.proizvodjac)


def homepage(request):
    return render(request, 'pocetna.html')

def SviPrinteri(request):
    try:

        lista_Printera = Printer.objects.all()

        context = {'lista_Printera':  lista_Printera}

    except Printer.DoesNotExist:
        raise Http404('Printers do not exist')

    return render(request, 'SviPrinteri.html', context=context)

def SvaPlastika(request):
    try:

        lista_plastike = Plastika.objects.all()

        context = {'lista_plastike':  lista_plastike}

    except Plastika.DoesNotExist:
        raise Http404('Plastic do not exist')

    return render(request, 'SvaPlastika.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')
