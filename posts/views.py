from django.shortcuts import render
from .models import Post, PostAttachment
# Create your views here.
def postList (request):
    posts = Post.objects.all()
    for post in posts:
        att = PostAttachment.objects.filter(post_id = post.pk)
        post.image = att
    return render(request, 'posts/post_list.html', {'posts':posts})

def postDetails(request, pid):
    post=Post.objects.get(pk=pid)
    images = PostAttachment.objects.filter(post_id = pid)
    return render(request, 'posts/details.html', {'post':post, 'images': images})