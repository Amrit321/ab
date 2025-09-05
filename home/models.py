from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.name