from django.urls import path
from .views import postList, postDetails
urlpatterns = [
    path('', postList, name='post-list'),
    path('<int:pid>/', postDetails, name='details-page'),
]