from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/predict/', predict_view, name='predict'),
    path('my-profile/', my_profile_view, name='my-profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
