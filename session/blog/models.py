from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100, default='')
    name = models.CharField(max_length = 20, default='')
    insta_id = models.URLField(max_length = 100, default='')
    email = models.EmailField(max_length = 30, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title