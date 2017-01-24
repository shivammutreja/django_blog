from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .forms import PostForm
from .models import Post

def post_create(request):
        form = PostForm(request.POST or None)
       
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "Item successfuly saved")
                return redirect(instance.get_absolute_url())
        else:
                messages.success(request, "Item wasn't saved")

        context = {
                "form": form,
                }
        
        return render(request, "post_form.html", context)


def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
            "instance": instance,
            "title": instance.title
            }
	return render(request, "detail.html", context)

def post_list(request):
	query_set = Post.objects.all()
	context = {
            "object_list": query_set,
            "title": "List"
            }
	return render(request, "base.html", context)

def post_update(request, id=None):
        instance = get_object_or_404(Post, id=id)

        form = PostForm(request.POST or None, instance=instance)
        
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "Item saved") 
                return redirect(instance.get_absolute_url())

        context = {
            "instance": instance,
            "title": instance.title,
            "form": form,
            }

        return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Item deleted") 
    return redirect("posts:list")


