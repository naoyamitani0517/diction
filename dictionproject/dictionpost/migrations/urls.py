from django.urls import path
from .views import BlogList,BlogDetail,topic_posts
from . import views
urlpatterns=[
    path('list/',BlogList.as_view(),name='list'),
    path('detail/<int:pk>/',BlogDetail.as_view(),name='detail'),
    path('topic_posts/<int:pk>/',views.topic_posts,name="post"),
]