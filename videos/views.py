from django.shortcuts import render, redirect
from .models import Video


def upload_video(request):

    if request.method == "POST":

        Video.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            thumbnail=request.FILES.get("thumbnail"),
            video=request.FILES.get("video"),
            status=request.POST.get("status"),
            duration=None
        )

        return redirect("video_list")

    return render(request, "video/video_upload.html")


def video_list(request):

    videos = Video.objects.all().order_by("-created_at")

    return render(
        request,
        "video/videolist.html",
        {
            "videos": videos
        }
    )