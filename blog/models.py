from users.models import User
from django.db import models
from django.urls import reverse


def upload_perfil_user(instance, filename):
    return f"profile_pictures/user_{instance.id}/{filename}"
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_perfil_user,)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})