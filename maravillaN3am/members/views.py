from django.shortcuts import render
from .models import Member

def members(request):  
    mymembers = Member.objects.all()  
    return render(request, 'index.html', {'mymembers': mymembers})  


def custom_404(request, exception):
    return render(request, '404.html', status=404)