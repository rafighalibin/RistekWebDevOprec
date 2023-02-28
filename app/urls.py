from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
     path('', views.homepage, name='homepage'),
     path('deleteTweet/<int:id>', views.deleteTweet, name='deleteTweet'),
     path('editTweet/<int:id>', views.editTweet, name='editTweet'),
]