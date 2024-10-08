from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))  # puts limit on status; human-readable vs integers


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # generates single line form
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()  # multi-line textarea input
    created_on = models.DateTimeField(auto_now_add=True)  # computer's time on save
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)  # validation will allow entry of an empty value
    updated_on = models.DateTimeField(auto_now=True)

    # The - prefix on created_on indicates the posts are displayed in descending order of creation date.
    class Meta:
        ordering = ["-created_on"]
        
    #  __str__() method has changed this post identifier to a string literal
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.author}"

