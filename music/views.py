from django.shortcuts import render, get_object_or_404
from .models import Album,Song
from django.views.generic.edit import CreateView,UpdateView,DeleteView


def fun(request):
    a=Album.objects.all()
    return render(request,"music/album.html",{"album":a})

def detail(request,ids):
    al=Album.objects.get(id=ids)
    s=al.song_set.all()
    return render(request, "music/song.html", {"songs": s,"album":al})


def fav(request,ids):
    al=get_object_or_404(Album,ids)
    return render(request,"music/fav.html",{'fav':al})

def play(request,soid):
    sp=Song.objects.get(id=soid)
    return render(request,"music/song.html",{"song":sp})

def regist(request):

    return render(request,"music/signup.html",{})

