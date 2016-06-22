
from django.conf.urls import url
from django.contrib import admin
from tweet.views import HomeView, crear_tweet, EditarTweet

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^crear_tweet/$', crear_tweet, name='crear-tweet'),
    url(r'^admin/', admin.site.urls),




    url(r'^update/tweet/(?P<id>[^/]+)$', EditarTweet.as_view(),
        name='editar-tweet'),
]
