from django.shortcuts import render

# Create your views here.


def index_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard/index.html', context)

def login_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'login.html', context)
