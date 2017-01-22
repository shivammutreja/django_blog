from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .forms import PostForm
from .models import Post

def post_create(request):
        form = PostForm(request.POST or None)
        
        context = {
                "form": form,
                }
        
        if form.is_valid():
                form.save(commit=False)
                form.save()
                
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

def post_update(request):
    return HttpResponse("<h3>Hello!</h3>")

def post_delete(request):
    return HttpResponse("<h3>Hello!</h3>")

