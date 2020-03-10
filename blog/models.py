from django.db import models
form django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "(%s) %s" %(self.user.username, self.post.title)
    