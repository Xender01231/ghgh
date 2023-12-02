from django.shortcuts import render. redirect
from blog.models import Post 

def posts_list(request):
    posts = Post.objects.all()
    return render(request, "blog/posts_list.html", {'posts': posts})
def post_like(request)
    if request.method =="POST"
        post_id = int(request.POST['post_id'])
        post = Post.objects.get(id=post_id)
        post.likes +- 1 
        post.save()
        return redirect("post_list")