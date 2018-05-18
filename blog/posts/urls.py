from django.urls import path

from .views import PostDetail, PostCreate, PostUpdate


app_name = 'posts'

urlpatterns = [
    path('create/', PostCreate.as_view(), name='create'),
    path('<int:pk>/', PostDetail.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='update')
]
