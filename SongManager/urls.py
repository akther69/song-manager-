"""
URL configuration for SongManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/add/',views.AlbumCreateView.as_view(),name="album-add"),
    path("album/all/",views.AlbumListView.as_view(),name="album-all"),
    path("album/<int:pk>/change/",views.AlbumUpdateView.as_view(),name="album-edit"),
    path("song/add/",views.SongCreateView.as_view(),name="song-add"),
    path("song/all/",views.SongListView.as_view(),name="song-all"),
    path("song/<int:pk>/change/",views.SongUpdateView.as_view(),name="song-edit"),
    path("song/<int:pk>/remove/",views.SongDeleteView.as_view(),name="song-remove"),
    path("album/<int:pk>/remove/",views.AlbumDeleteView.as_view(),name="album-delete"),
    path("album/<int:pk>/details",views.AlbumDetailView.as_view(),name="album-details"),
    path("register/",views.SignUpView.as_view(),name="sign-up"),
    path("",views.SignInView.as_view(),name="sign-in"),
    path("logout/",views.SignOutView.as_view(),name="sign-out")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
