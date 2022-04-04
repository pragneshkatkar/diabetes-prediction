from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import logout

from main.models import DietBlog, Doctor, Feedback, Prediction, UsersAddress

# Create your views here.
@login_required(login_url='/login/')
def index_view(request):
    user_id = request.session['user_id']
    predictions = Prediction.objects.filter(user_id=user_id).values().order_by('-id')
    user = User.objects.filter(id=user_id).values()[0]
    context = {
        'title': 'Home',
        'predictions': predictions,
        'user': user
    }
    return render(request, 'dashboard/index.html', context)


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
    user_id = request.session['user_id']
    predictions = Prediction.objects.filter(user_id=user_id).values().order_by('-id')
    user = User.objects.filter(id=user_id).values()[0]
    context = {
        'title': 'Home',
        'predictions': predictions,
        'user': user
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='/login/')
def predict_view(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'dashboard/predict.html', context)


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    context = {
        'title': 'Home'
    }
    return redirect('/login/')

def prediction_view(request, id):
    prediction = Prediction.objects.filter(id=id).values()[0]
    context = {
        'title': 'Home',
        'prediction': prediction
    }
    return render(request, 'dashboard/prediction.html', context)


@login_required(login_url='/login/')
def my_profile_view(request):
    user_id = request.session['user_id']
    user = User.objects.filter(id=user_id).values()[0]
    address = UsersAddress.objects.filter(user_id=user_id).values()
    if address:
        address = address[0]
    context = {
        'title': 'Home',
        'user': user,
        'address': address
    }
    return render(request, 'my-profile.html', context)
    

@login_required(login_url='/login/')
def doctors_contacts(request):
    doctors = Doctor.objects.all().values()
    context = {
        'title': 'Home',
        'doctors': doctors
    }
    return render(request, 'admin-dashboard/doctors-contact.html', context)

@api_view(['GET', 'POST'])
def doctors_contacts_add(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'admin-dashboard/add-doctor.html', context)


@login_required(login_url='/login/')
def feedback_view(request):
    user_id= request.session['user_id']
    user = User.objects.filter(id=user_id).values()[0]
    feedback = Feedback.objects.filter(user_id=user_id)
    if user['is_superuser']:
        feedback = Feedback.objects.all()
    context = {
        'title':  'Feedback',
        'feedbacks': feedback
    }
    return render(request, 'dashboard/feedback.html', context)

def users_predictions_view(request):
    user_id = request.session['user_id']
    user = User.objects.filter(id=user_id).values()[0]
    if user['is_superuser']:
        predictions = Prediction.objects.all().order_by('-id')
    context = {
        'title': 'Home',
        'predictions': predictions
    }
    return render(request, 'admin-dashboard/users-predictions.html', context)


def users_view(request):
    user_id = request.session['user_id']
    user = User.objects.filter(id=user_id).values()[0]
    if user['is_superuser']:
        users = User.objects.all()
    context = {
        'title': 'Home',
        'users': users
    }
    return render(request, 'admin-dashboard/users.html', context)

def diets_view(request, id=None):
    diets = DietBlog.objects.all().values()
    if id is not None:
        diet = DietBlog.objects.filter(id=id).values()[0]
        context = {
            'title': 'Home',
            'diet': diet,
            'user': request.user
        }
        return render(request, 'admin-dashboard/add-diet.html', context)
    context = {
        'title': 'Home',
        'diets': diets,
        'user': request.user
    }
    return render(request, 'dashboard/diets.html', context)

def add_diet_view(request):
    context = {
        'title': 'Home',
    }
    if request.user.is_superuser:
        return render(request, 'admin-dashboard/add-diet.html', context)
    return redirect('/diets/')
