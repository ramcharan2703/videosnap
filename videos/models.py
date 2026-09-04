from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):

    STATUS_CHOICES = (
        ("public", "Public"),
        ("private", "Private"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="videos"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="videos/"
    )
    duration = models.DurationField(
    null=True,
    blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="public"
    )

    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title