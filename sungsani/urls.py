from django.urls import path
from django.conf.urls import url
from . import views

app_name = "sungsani"
urlpatterns = [
    path('', views.index2, name="index"),
    path('memo/', views.memo_index, name="memo_index"),
    path('blog/', views.post_list, name="post_list"),
    path('blog/<int:pk>/', views.post_detail, name="post_detail"),
    path('blog/new/', views.post_new, name = "post_new"),
    path('blog/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/drafts/', views.post_draft_list, name='post_draft_list'),
    path('blog/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('blog/<int:pk>/remove/', views.post_remove, name='post_remove'),
]