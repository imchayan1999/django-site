from django.urls import path

from . import views



urlpatterns = [
    path('signup/', view.SignUp.as_view(), name='signup'),
]
