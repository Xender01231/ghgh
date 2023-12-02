from django.contrib import admin
from django.urls import path
from fitness.views import index, magic_number
from blog.views import posts_list, post_like
from playlist.views import playlist
from django.conf.urls.static import static
from django.conf import settings
from playlist.views import createvideo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('magic_number/', magic_number),
    path('blog/', posts_list, name='post_list'),
    path('playlist/', playlist, name="play_list"),
    path('createvideo/',createvideo),
    path('blog/post_like/', post_like, name='post_like'),
    path('blog/post_list', posts_list, name='post_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)