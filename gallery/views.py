from django.shortcuts import render ,get_object_or_404
from .forms import FormUploadImage

from .models import Post ,PostImage
# Create your views here.


def blog_view(request):
    posts = Post.objects.all()

    return render(request, 'gallery/post.html',{'posts':posts})

def detail_view (request,id):
    post = get_object_or_404(Post,id=id)

    photos = PostImage.objects.filter(post=post)
    return render(request, 'gallery/post_detail.html',{
        'post':post,
        'photos':photos,    
    })