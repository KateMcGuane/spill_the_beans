from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a paginated list of six posts
    per page.

    **Context**
    ``queryset``
        All published instances of :model:`blog.Post`.
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html`
        Renders the list of published posts in
        a paginated format.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


# Function-based view
def post_detail(request, slug):

    """
    Display details an individual :model:`blog.Post`,
    and its approved comments.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        Number of approved comments related to the post.
    ``comment_form``
        A form to submit new comments for the post.
        An instance of :form:`blog.CommentForm`.

    **Template:**
    :template:`blog/post_detail.html`
        Renders the post details, approved comments,
        and the comment submission form.
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    # Resets content of the form
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
            "comment_form": comment_form
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Allows user to edit own comment on post.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        The commetn to be edited.
    ``comment_form``
        A form pre-populated with the comment's data for editing.
        An instance of :form:`blog.CommentForm`.

    **Template:**
    :template:`blog/post_detail.html`
        Renders post details & comment edit form (if applicable).
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Allows user to delete own comment on post.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        The comment to be deleted.

    **Template:**
    :template:`blog/post_detail.html`
        Renders the post details after a comment is deleted
        (or error if not owned by the user).
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
