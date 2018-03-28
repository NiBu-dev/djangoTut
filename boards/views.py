from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.


def home(requests):
    boards = Board.objects.all()

    return render(requests, 'home.html', {'boards': boards})


