from django.shortcuts import render, get_object_or_404
from .models import Game, Genre

def game_list(request):
    genre_slug = request.GET.get('genre', '')
    platform = request.GET.get('platform', '')
    query = request.GET.get('q', '')
    genres = Genre.objects.all()
    games = Game.objects.all()

    if genre_slug:
        games = games.filter(genre__slug=genre_slug)
    if platform:
        games = games.filter(platform=platform)
    if query:
        games = games.filter(name__icontains=query)

    return render(request, 'games/game_list.html', {
        'games': games,
        'genres': genres,
        'current_genre': genre_slug,
        'current_platform': platform,
        'query': query,
    })

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

# Create your views here.
