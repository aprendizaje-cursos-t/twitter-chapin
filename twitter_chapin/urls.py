from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from tweet.views import HomeView, crear_tweet, EditarTweet, CrearTweet, EliminarTweet, lista_tweet
from tweet.views import TweetRealTime
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^crear_tweet/$', crear_tweet, name='crear-tweet'),
    url(r'^admin/', admin.site.urls),

    url(r'^update/tweet/(?P<id>[^/]+)$', EditarTweet.as_view(),
        name='editar-tweet'),
    url(r'^create/tweet/$', CrearTweet.as_view(),
        name='tweet-nuevo'),
    url(r'^delete/tweet/(?P<id>[^/]+)$', EliminarTweet.as_view(),
        name='eliminar-tweet'),
    url(r'^api/lista-tweet/$', lista_tweet,
        name='api-lista-tweet'),
    url(r'^real-time/$', TweetRealTime.as_view(),
        name='real-time'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
