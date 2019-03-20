from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Music


def index(request):
    all_album = Album.objects.all()
    return render(request, "music/index.html", {"all_album": all_album})


def detail(request, album_id):
    # try:
    #     album1 = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album Does not exist")
    album1 = get_object_or_404(Album, pk=album_id)
    return render(request, "music/detail.html", {"album1": album1})


def favourite(request, album_id):
    album1 = get_object_or_404(Album, pk=album_id)
    try:
        song_detail = album1.music_set.get(pk=request.POST['song'])
    except (KeyError, Music.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album1': album1,
            'error_message': "Please select a valid song"
        })
    else:
        song_detail.is_favourite = True
        song_detail.save()
        return render(request, 'music/detail.html', {"album1": album1})
