from django.shortcuts import render
from main_atelier.models import Service

# Create your views here.


def service_info(request, pk):
    favor = Service.objects.get(pk=pk)
    return render(request, 'service.html', context={'favor': favor})
