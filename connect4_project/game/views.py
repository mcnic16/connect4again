from django.shortcuts import render

def connect4_view(request):
    return render(request, 'game/connect4.html')