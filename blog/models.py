from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return "(%s) %s" %(self.user.username, self.post.title)
    