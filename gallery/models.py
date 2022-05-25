from django.db import models



class Post(models.Model):
    # category = models.ForeignKey('Categorys', on_delete=models.CASCADE ,null=True,blank=True)



    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.title)



class PostImage(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.post.title)



class PostImageAuthor(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)