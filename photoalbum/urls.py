from django.urls import path
from . import views

#my
from .views import Album_Create,DeleteAlbum,UpdateAlbum


app_name = 'photoalbum'
urlpatterns = [
    path('', views.albumfunc,name='index'),
    path('create/', views.Album_Create.as_view(),name='create'),
    path('<int:id>/delete/',views.DeleteAlbum.as_view(),name='delete'),
    path('<int:id>/update/',views.UpdateAlbum.as_view(),name='update'),
]
