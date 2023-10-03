from django.urls import path
from another_app.views import *

app_name = 'another_app'

urlpatterns = [
    path('contact', contact_view , name='contact')
]