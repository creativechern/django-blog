from django.db import models
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField

class Post(models.Model):

    title = models.CharField(max_length = 250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE,
    )
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})




