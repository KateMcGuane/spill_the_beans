from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


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

    # Helper function render() returns HttpResponse object
    return render(
        request,
        "blog/post_detail.html",
        # Context
        {"post": post},
    )