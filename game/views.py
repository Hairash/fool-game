from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={'counter': 0, 'players_counter': 0})
