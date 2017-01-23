from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .forms import PostForm
from .models import Post

def post_create(request):
        form = PostForm(request.POST or None)
       
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return HttpResponseRedirect(instance.get_absolute_url())

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
	return render(request, "index.html", context)

def post_update(request, id=None):
        instance = get_object_or_404(Post, id=id)

        form = PostForm(request.POST or None, instance=instance)
        
        if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "instance": instance,
            "title": instance.title,
            "form": form,
            }

        return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("<h3>Hello!</h3>")

