from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from posts.utils import youtube

class PostCreateFormView(View): 

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "posts/new.html",
                context={},
        )


class PostCreateConfirmView(View):
    
    def get(self, request, *args, **kwargs):
        return redirect(reverse("post:create"))
    
    def post(self, request, *args, **kwargs):
        video_id = request.POST.get("video_id")
        title = request.POST.get("title")
        content = request.POST.get("content")

        return render(
                request,
                "posts/confirm.html",
                context={
                    "title":title,
                    "content":content,
                    "video_id":video_id,

                    "youtube_original_url":youtube.get_youtube_original_url(video_id),
                    "youtube_embed_url":youtube.get_youtube_embed_url(video_id),
                    },
        )
