from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """A blog category or section."""
    name = models.CharField(max_length=200)  # Blog title/category name
    date_added = models.DateTimeField(auto_now_add=True)  # When created
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the blog name as its string representation."""
        return self.name 

class BlogPost(models.Model):
    """A user post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posts = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
            """Return a simple string representing the post."""
            return f"{self.posts[:50]}..."