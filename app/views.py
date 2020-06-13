from django.shortcuts import render
from app.models import FileSystem


# Create your views here.
def index(request):
    return render(request, 'index.html', {'filesystem': FileSystem.objects.all()})
