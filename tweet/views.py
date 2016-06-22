from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User
import datetime
from django import forms
from django.core.urlresolvers import reverse
from django.contrib import messages


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

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, 'Has cambiando tu tweet.')

        return reverse('editar-tweet', args=[self.object.id])
