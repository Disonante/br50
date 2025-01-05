from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tirada
from .forms import TiradaForm

def inicio(request):
    return render(request, 'inicio.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loguear automáticamente al usuario tras el registro
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('tiradas')  # Redirigir a la página de tiradas tras el registro
        else:
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


@login_required
def tiradas(request):
    tiradas = Tirada.objects.all()
    return render(request, 'tiradas.html', {'tiradas': tiradas})

@login_required
def nueva_tirada(request):
    if request.method == 'POST':
        form = TiradaForm(request.POST)
        if form.is_valid():
            tirada = form.save(commit=False)
            tirada.usuario = request.user
            tirada.save()
            return redirect('tiradas')
    else:
        form = TiradaForm()
    return render(request, 'tirada_form.html', {'form': form})

@login_required
def editar_tirada(request, pk):
    tirada = Tirada.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TiradaForm(request.POST, instance=tirada)
        if form.is_valid():
            form.save()
            return redirect('tiradas')
    else:
        form = TiradaForm(instance=tirada)
    return render(request, 'tirada_form.html', {'form': form})

@login_required
def eliminar_tirada(request, pk):
    tirada = Tirada.objects.get(pk=pk, usuario=request.user)
    tirada.delete()
    return redirect('tiradas')


# GRAFICOS

from django.shortcuts import render

from .models import Tirada

from django.db.models import Sum
import json

def graficas_view(request):
    # Agregar lógica para agrupar las puntuaciones y dieces por usuario
    data = (
        Tirada.objects.values("user__username")
        .annotate(total_puntuacion=Sum("puntuacion"), total_dieces=Sum("n_dieces"))
        .order_by("user__username")
    )

    # Serializar los datos para pasarlos al frontend
    usuarios = [item["user__username"] for item in data]
    puntuaciones = [item["total_puntuacion"] for item in data]
    dieces = [item["total_dieces"] for item in data]

    context = {
        "usuarios": json.dumps(usuarios),
       
        "puntuaciones": json.dumps(puntuaciones),
        "dieces": json.dumps(dieces),
    }
    return render(request, "graficas.html", context)


#GRAFICA

# views.py
import json
from django.shortcuts import render
from .models import Tirada

def tiradas(request):
    tiradas = Tirada.objects.all()  # Obtenemos todas las tiradas
    # Preparamos los datos que necesitamos para la gráfica
    tiradas_data = [
        {
            'tirador': tirada.tirador,
            'fecha': tirada.fecha.strftime('%Y-%m-%d'),  # Convertimos la fecha a formato 'YYYY-MM-DD'
            'puntuacion': float(tirada.puntuacion),  # Convertir Decimal a float
            'numero_dieces': int(tirada.numero_dieces)  # Convertir a entero si es necesario
        }
        for tirada in tiradas
    ]
    # Convertimos los datos a JSON y lo pasamos al contexto
    tiradas_data_json = json.dumps(tiradas_data)
    return render(request, 'tiradas.html', {'tiradas': tiradas, 'tiradas_data': tiradas_data_json})
