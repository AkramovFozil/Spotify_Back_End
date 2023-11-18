from django.urls import path
from .views import ArtistList, ArtistDetail, AlbumList, AlbumDetail, SongList, SongDetail, get_songs_for_album

urlpatterns = [
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name='artist-detail'),
    path('albums/', AlbumList.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
    path('songs/', SongList.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongDetail.as_view(), name='song-detail'),
    path('albums/<int:album_id>/songs/',get_songs_for_album,name='get-songs-for-album'),
]