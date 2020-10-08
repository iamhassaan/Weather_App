from django.shortcuts import render

# just for the sake of github.

def home(request):
    return render(request, 'home.html', {})    

    
def about(request):
    return render(request, 'about.html', {})    