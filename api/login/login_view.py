from django.shortcuts import render


def login_view(request):
    template_name = "index.html"
    return render(request,template_name)