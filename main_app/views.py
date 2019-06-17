
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Profile, Character, Game, User
# from django.contrib.auth.models import User


# Create your views here.
def home(request):
  return render(request, 'home.html')

def profile(request):
    user = request.user
    games = Game.objects.all()
    return render(request, 'profile.html',{'games':games})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_page')
        else:
            error_message = 'You Shall Not Pass! - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
  
def characters_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'characters/detail.html', {'character': character})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game': game})

class CharacterCreate(CreateView):
    model = Character
    fields = ['name']

class GameCreate(CreateView):
    model = Game
    fields = ['name', 'description']
