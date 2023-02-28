from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Tweet
from .serializers import TweetSerializer
from rest_framework import status

@api_view(['GET'])
def get(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    if request.data.__getitem__("tweet") != "":
        new_tweet = Tweet(
            content = request.data.__getitem__("tweet"),
            creator = request.COOKIES.get('user_token')
        )
        new_tweet.save()
    serializer = TweetSerializer(new_tweet)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    user_token = request.COOKIES.get('user_token')
    tweet = Tweet.objects.filter(id=id)[0]
    if tweet == None:
        return Response({"status": "fail"}, status=status.HTTP_404_NOT_FOUND)

    if user_token == tweet.creator:
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response({"status": "fail"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def edit(request, id):
    user_token = request.COOKIES.get('user_token')
    tweet = Tweet.objects.filter(id=id)[0]
    if user_token == tweet.creator:
        tweet.content = request.data.__getitem__("tweet")
        tweet.save()
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)
    
    return Response({"status": "fail"}, status=status.HTTP_404_NOT_FOUND)
    
    