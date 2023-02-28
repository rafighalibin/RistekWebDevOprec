from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from api.views import *
from django.views.decorators.csrf import csrf_exempt
import json
import requests 

@csrf_exempt
def homepage(request):
    user_token = request.COOKIES.get('user_token')
    if user_token is None:
        generated_user_token = get_random_string(length=32)
        response = HttpResponseRedirect(reverse("app:homepage"))
        response.set_cookie('user_token', generated_user_token)
        return response

    if request.method == "POST":
        requests.post('http://127.0.0.1:8000/api/add/', data=request.body, headers=request.headers)
             
    tweets = json.loads(requests.get('http://127.0.0.1:8000/api/get/?format=json').content)
    context = {
        'user_token': user_token,
    }
    return render(request, 'homepage.html', context)

@csrf_exempt
def deleteTweet(request, id):
    # TODO: response
    user_token = request.COOKIES.get('user_token')
    requests.delete('http://127.0.0.1:8000/api/delete/'+str(id), headers=request.headers)
    context = {
        'user_token': user_token,
        'response': "response",
    }
    return redirect('app:homepage')


@csrf_exempt
def editTweet(request, id):
    user_token = request.COOKIES.get('user_token')
    
    if request.method == "POST":
        requests.put('http://127.0.0.1:8000/api/edit/'+str(id), data=request.body, headers=request.headers)
        return redirect('app:homepage')

    tweet = Tweet.objects.filter(id=id)[0]
    user_token = request.COOKIES.get('user_token')
    if user_token == tweet.creator:
        context = {
            'user_token': user_token,
            'content': tweet.content,
        }
        return render(request, 'homepage.html', context)
    
    context = {
            'user_token': user_token,
            'message': 'You can only edit you own tweet!'
        }
    return render(request, 'homepage.html', context)