from django.shortcuts import render

from .models import Thread, Post

def index(request):
    thread = Thread.objects.order_by('created_at')
    context = {
        'threads': thread,
    }
    return render(request, 'forum/index.html', context)

def thread(request, thread_id):
    if request.method == 'POST':
        post = Post(
            thread = Thread.objects.get(pk=thread_id),
            author = request.user,
            content = request.POST['content'],
        )
        post.save()
    
    thread = Thread.objects.get(pk=thread_id)
    posts = Post.objects.filter(thread=thread)
    context = {
        'thread': thread,
        'posts': posts,
    }
    return render(request, 'forum/thread.html', context)

def new_thread(request):
    if request.method == 'POST':
        thread = Thread(
            title = request.POST['title'],
            author = request.user,
        )
        thread.save()
        return render(request, 'forum/thread.html', {'thread': thread})
    else:
        return render(request, 'forum/new.html')