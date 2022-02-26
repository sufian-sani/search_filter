from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post_details/<pk>/<slug>/', PostDetailView.as_view(), name='post_details'),
    path('search/', search, name='search'),
    path('filter/', filter, name='filter'),
]
