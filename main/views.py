from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'index.html', context)


def login_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'login.html', context)


def dashboard_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard/index.html', context)


def predict_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard/predict.html', context)


def my_profile_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'my-profile.html', context)
