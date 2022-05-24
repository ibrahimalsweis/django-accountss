from django.db import models



class Post(models.Model):
    # category = models.ForeignKey('Categorys', on_delete=models.CASCADE ,null=True,blank=True)



    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return str(self.title)



class PostImage(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.post.title)
