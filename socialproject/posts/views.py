from django.shortcuts import render, redirect
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.

@login_required
def post_create(request):
    # handle POST request to create a new post
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        # display the form for creating a new post
        form = PostCreateForm(data=request.GET)
    
    # render the create post page with the form
    return render(request, 'posts/create.html', {'form' : form})

def feed(request):
    # handle POST request to add a new comment to a post
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        # Display an empty comment form
        comment_form = CommentForm()
    
    #retrieve all posts and the logged-in user
    posts = Post.objects.all()
    logged_user = request.user
    
    # render the feed page with posts, logged-in user, and comment form
    return render(request, 'posts/feed.html', {'posts' : posts, 'logged_user' : logged_user, 'comment_form' : comment_form})

def like_post(request):
    # handle AJAX request to like/unlike a post
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    
    # toggle like/unlike for the logged-in user
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    
    # redirect to the feed page after updating likes
    return redirect('feed')
