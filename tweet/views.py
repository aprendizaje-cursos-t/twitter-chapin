from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User
import datetime
from django import forms
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import json


class HomeView(ListView):
    model = Tweet
    template_name = "home.html"
    context_object_name = "todos"
    ordering = ('-date',)

    def get_context_data(self, **kwargs):
        data = super(ListView, self).get_context_data(**kwargs)

        mi_hermano = TweetForm()
        data['variable'] = mi_hermano

        return data


def crear_tweet(request):
    if request.method == "POST":
        tweet = Tweet()
        tweet.user = request.user
        tweet.text = request.POST['text']
        tweet.save()
    return HttpResponseRedirect('/')


class EditarTweet(UpdateView):
    model = Tweet
    template_name = "editar.html"
    slug_field = 'id'
    slug_url_kwarg = 'id'
    success_url = "/"
    context_object_name = 'form_editar'
    form_class = TweetForm

    def get_form(self, form_class=None):
        form = super(EditarTweet, self).get_form(form_class)
        form.fields['user'].widget = forms.HiddenInput()
        return form

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, 'Has cambiando tu tweet.')

        return reverse('editar-tweet', args=[self.object.id])


class CrearTweet(CreateView):
    model = Tweet
    template_name = 'editar.html'
    form_class = TweetForm
    context_object_name = 'form_editar'

    def get_form(self, form_class=None):
        form = super(CrearTweet, self).get_form(form_class)
        return form


class EliminarTweet(DeleteView):
    model = Tweet
    template_name = 'eliminar.html'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'id'
    slug_field = 'id'
    context_object_name = 'tweet'
    success_url = '/'


class TweetRealTime(TemplateView):
    template_name = 'tweets_real_time.html'


def lista_tweet(request):
    todos = Tweet.objects.all().order_by('-id')
    tweets = []
    for tweet_actual in todos:
        tweets.append({
                "id": tweet_actual.id,
                "text": tweet_actual.text,
                "user": tweet_actual.user.username
            })
    return HttpResponse(
        json.dumps(tweets), content_type="application/json"
    )


