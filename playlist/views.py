from django.shortcuts import render
from .models import Video

def playlist(request):
    videos = Video.objects.all() 
    return render(request, "playlist/playlist.html", {'videos' : videos})

def  createvideo(request):
    return render(request, "playlist/createvideo.html")

def createvideo(request):
    if request.method == "POST":
        embed_code = request.POST['embed_code']
        name = request.POST['name']
        Video.objects.create(
            name=name,
            embed_code=embed_code
        )
    return render(request, "playlist/createvideo.html",)

