from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/predict/', predict_view, name='predict'),
    path('dashboard/prediction/', prediction_view, name='prediction'),
    path('my-profile/', my_profile_view, name='my-profile'),
    path('admin/doctors-contacts/', doctors_contacts, name='doctors-contact'),
    path('admin/doctors-contacts/add/', doctors_contacts_add, name='doctors-contact'),
    path('admin/doctors-contacts/edit/', doctors_contacts_add, name='doctors-contact'),
    path('admin/users-predictions/', users_predictions, name='users-predictions'),
    path('admin/users/', users, name='users'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
