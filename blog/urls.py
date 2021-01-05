
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView,CreatePost, UpdatePostView,DeletePostView,CreateCategory, CategoryViews,LikeView,AddCommentView
urlpatterns = [
    #path('', views.home, name = 'home'),
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article'),
    path('add/', CreatePost.as_view(), name = 'add_post'),
    path('add_category/', CreateCategory.as_view(), name = 'add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryViews, name = 'category'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment')
]
