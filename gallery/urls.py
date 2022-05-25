from django.urls import path 
from . import views






app_name = 'gallery'
urlpatterns = [
    path('',views.blog_view,name='blog_view'),
    path('/<int:id>',views.detail_view,name='detail_view'),
]