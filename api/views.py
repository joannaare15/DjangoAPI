from django.shortcuts import render

def detail_view(request):
    return render(request, 'detail.html')  # Asegúrate de que este archivo exista en tu directorio de plantillas
