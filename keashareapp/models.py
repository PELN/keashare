from django.db import models
from django.contrib.auth.models import User

class AppGroup(models.Model):
    # Meta
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners')
    users = models.ManyToManyField(User) # members
    # Data
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    # Meta
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(AppGroup, on_delete=models.CASCADE)
    # Data
    last_updated = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:20] # show 20 characters