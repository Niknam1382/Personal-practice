from django.http import HttpResponse

# Create your views here.
def contact_view(request) :
    return HttpResponse('<h2>This is contact</h2>')