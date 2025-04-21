from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    """
    Represents an About section for the site or user.

    Stores information such as a title, profile image,
    and descriptive content. Automatically tracks when
    the content was last updated.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the About entry.

        Displays the title of the About section.
        """
        return self.title


class CollaborateRequest(models.Model):
    """
    Represents a collaboration request submitted by a visitor.

    Stores the visitor's name, email, message content, and whether
    the message has been marked as read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the collaboration request.

        Displays the requestor's name for easy identification.
        """
        return f"Collaboration request from {self.name}"
