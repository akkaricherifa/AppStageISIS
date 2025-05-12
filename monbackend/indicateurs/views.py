from django.shortcuts import render
from .models import Indicateur
import pandas as pd
# Create your views here.
import pandas as pd
from django.shortcuts import render
from .models import Indicateur

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


def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html') 

def interface(request):
    return render(request, 'interface.html') 