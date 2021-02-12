from django.urls import path

from .views import (
        BlogListView,
        BlogDetailView, 
        BlogCreateView,
        BlogUpdateView, 
        )

urlpatterns = [ 
        path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='post_update'),
        path('post/create/', BlogCreateView.as_view(), name='post_create'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('', BlogListView.as_view(), name='home'),
        ]
