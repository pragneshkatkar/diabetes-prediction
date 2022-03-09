from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from main.models import Prediction

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


def signup_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'signup.html', context)


@api_view(['POST', 'PUT', 'GET'])
def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            password=request.data['password'],
            username=request.data['username'])
        user.save()
        return Response()
    elif request.method == 'PUT':
        user = User.objects.get(id=request.data['user_id'])
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.username = request.data['username']
        user.save()
        return Response()
    else:
        return render(request, 'signup.html')


@login_required(login_url='/login/')
def dashboard_view(request):
    predictions = Prediction.objects.all().values().order_by('-id')
    context = {
        'title': 'Home',
        'predictions': predictions
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='/login/')
def predict_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard/predict.html', context)

def prediction_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard/prediction.html', context)


def my_profile_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'my-profile.html', context)
    

def doctors_contacts(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'admin-dashboard/doctors-contact.html', context)

@api_view(['GET', 'POST'])
def doctors_contacts_add(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'admin-dashboard/add-doctor.html', context)


def users_predictions(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'admin-dashboard/users-predictions.html', context)


def users(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'admin-dashboard/users.html', context)