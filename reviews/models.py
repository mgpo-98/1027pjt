from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to="images/", blank=True, null=True, processors=[ResizeToFill(400, 300)],
    format = 'JPEG', options={'quality':80})
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    review = models.ForeignKey(Review,on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)