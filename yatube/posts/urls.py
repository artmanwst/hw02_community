from django.urls import path, include

from .import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('auth/', include('users.urls')),   
    path('auth/', include('django.contrib.auth.urls')),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('posts/<int:post_id>/',views.post_detail,name='post_detail'),
    path('create/',views.post_create,name='post_create'),
    path('edit/<int:post_id>/',views.post_edit,name='post_ed')
]
