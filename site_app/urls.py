from django.urls import path
from site_app.views import *

app_name = 'site_app'

urlpatterns = [
    path('', index, name='index')
]