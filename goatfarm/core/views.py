from django.shortcuts import render, redirect
from .models import Goat
from .forms import GoatForm

def home(request):
    goats = Goat.objects.all()
    return render(request, 'core/home.html', {'goats': goats})

def example_view(request):
    return render(request, 'core/example.html')

def add_goat(request):
    if request.method == 'POST':
        form = GoatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GoatForm()
    return render(request, 'core/add_goat.html', {'form': form})

def example_view(request):
    return render(request, "core/example.html")
