from django.shortcuts import render
from .models import Indicateur
import pandas as pd
# Create your views here.
import pandas as pd
from django.shortcuts import render
from .models import Indicateur
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt

def importer_excel(request):
    if request.method == "POST":
        file = request.FILES['excel_file']
        df = pd.read_excel(file)

        for index, row in df.iterrows():
            Indicateur.objects.create(
                titre=row['Titre'],
                description=row.get('Description', ''),
                valeur=row['Valeur'],
                unite=row['Unite'],
                date_mesure=row['DateMesure'],
            )

        return render(request, 'import_success.html')

    return render(request, 'importer.html')

def connexion_superadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Tentative de connexion : {username}, {password}")
        # Authentification
        user = authenticate(request, username=username, password=password)
        print("Résultat de authenticate :", user)
        
        if user is not None and user.is_superuser:
            login(request, user)
            print("Login OK")
            return redirect('/interface/')  # Redirige vers l'interface admin
        else:
            print("Login échoué")
            messages.error(request, "Identifiants incorrects ou vous n'avez pas les droits d'administration")
    
    return render(request, 'connexion.html')




def is_superadmin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_superadmin)
def interface_admin(request):
    return render(request, 'interface.html')


def home(request):
    return render(request, 'connexion.html')

def home2(request):
    return render(request, 'home2.html') 

def interface(request):
    return render(request, 'interface.html') 

