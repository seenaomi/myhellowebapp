from django.shortcuts import render
from collection.models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {
		'posts': posts,
		})

def post_detail(request, slug):
    # grab the object
    post = Post.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'posts/post_detail.html', {
    	'post': post,
    	})	