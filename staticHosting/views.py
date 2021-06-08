from django.shortcuts import render


def helloView(request, name):
    return render(request, 'home.html', {'name': name})
