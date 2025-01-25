from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm


# Create your views here.
# Class-based view
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


# Function-based view
def post_detail(request, slug):

    """
    Display an individual :model:`blog.Post`.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.

    **Template:**
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    # Helper function get_object_or_404
    # Get data or raise a Http404 error if data object does not exist
    # The variable assigned to the result
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    comment_form = CommentForm()

    # Helper function render() returns HttpResponse object
    return render(
        request,
        "blog/post_detail.html",
        # Context
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )