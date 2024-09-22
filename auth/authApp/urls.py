from django.urls import path
from .views import *

urlpatterns = [
    path('signin',auth,name='signin'),
]