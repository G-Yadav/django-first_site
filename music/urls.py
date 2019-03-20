from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # path to music Album view index page /music/
    path('', views.index, name="index"),

    # path to music Song view page /music/34/
    path('<int:album_id>/', views.detail, name="detail"),

    # path to add favourite song /music/album.id/
    path('<int:album_id>/favourite/', views.favourite, name="favourite")
]
