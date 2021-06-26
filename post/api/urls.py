from django.urls import path

from post.api import views as api_views


urlpatterns = [
    path('posts/',api_views.PostView.as_view(), name='post_list'),
    path('images/',api_views.PostImageView.as_view(), name='post_images_list'),
    path('post/<int:pk>', api_views.PostDetailView.as_view(), name='post_detail'),
]

