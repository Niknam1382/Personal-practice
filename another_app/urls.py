from django.urls import path
from another_app.views import *

app_name = 'another_app'

urlpatterns = [
    path('', contact_view , name='contact')
]