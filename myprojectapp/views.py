from django.shortcuts import render

# Create your views here.
def myprojectapp(request):
    return render(request, 'index.html', {})
