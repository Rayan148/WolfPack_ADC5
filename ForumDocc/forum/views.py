from django.shortcuts import render, redirect
from .forms import ThreadForm, ReplyForm
from django.contrib.auth.decorators import login_required
from .models import Thread


def thread(request, thread_id):
    thread=Thread.objects.get(pk=thread_id)

    if request.method=='POST':  #For reply
        form=ReplyForm(request.POST)
        form=ReplyForm(request.POST)
        reply=form.save(commit=False)
        reply.thread=thread
        reply.user=request.user
        reply.save()
        return redirect('forum:thread', thread_id=thread_id)
    else:
        form=ReplyForm()

    context={'thread':thread, 'form':form}
    return render(request, 'forum/thread.html', context)


@login_required
def new_thread(request):
    form=ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user:home')
        else:
            return redirect('forum:new_thread')
    else:
        return render(request, 'forum/ask_thread.html', {'form':form})

@login_required
def delete_thread(request, pk):
    if request.method=="POST":
        thread= Thread.objects.get(pk=pk)
        thread.delete()
    return redirect('user:home')
