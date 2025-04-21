from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Puts limit on status; human-readable vs integers
STATUS = (
    (0, "Draft"),
    (1, "Published"),
)


# Create your models here.
class Post(models.Model):
    """
    Represents a blog post created by a user.
    Stores a single blog post entry related to :model:`auth.User`.
    Post model is a subclass of Django's Model class.
    Defines the fields and behaviors of the blog post.

    Each post includes a title, slug (URL-friendly identifier),
    author, featured image, content, optional excerpt, timestamps,
    and a status indicating whether it's a draft or published.

    Timestamps = Computer's time on save.
    """
    title = models.CharField(
        max_length=200, unique=True
    )  # generates single line form
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()  # multi-line textarea input
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the Post model.

        Orders posts by the created_on field in descending order,
        so the most recent posts appear first.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the post.

        Includes the post title and the author's name.
        Useful for display in the Django admin and debug output.
        """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Represents a comment made by a user on a blog post.

    Each comment is linked to a specific post and user,
    includes the comment body, approval status, and timestamp.

    Comments are ordered by creation date in ascending order.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
