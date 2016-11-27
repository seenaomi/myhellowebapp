from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import PostForm
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

@login_required
def edit_post(request, slug):
    # grab the object
    post = Post.objects.get(slug=slug)
    # make sure the logged in user is the owner of the thing
    if post.user != request.user:
        raise Http404

    # set the form we're using
    form_class = PostForm
    # if we're coming to this view from a submitted form,
    if request.method == 'Post':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('post_detail', slug=post.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=post)

    # and render the template
    return render(request, 'posts/edit_post.html', {
    	'post': post,
    	'form': form,
    })

def create_post(request):
    form_class = PostForm
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            post = form.save(commit=False)
            # set the additonal details
            post.user = request.user
            post.slug = slugify(post.title)
            # save the object
            post.save()
            # redirect to our newly created post
            return redirect('post_detail', slug=post.slug)
            # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'posts/create_post.html', {
        'form': form,
    })

def browse_by_title(request, initial=None):
    if initial:
        posts = Post.objects.filter(
            title__istartswith=initial).order_by('title')
    else:
        posts = Post.objects.all().order_by('title')
    return render(request, 'search/search.html', {
        'posts': posts,
        'initial': initial,
    })                  
