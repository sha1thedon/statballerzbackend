from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from statballerz.models import Central, GoalKeeper, Player, PlayerLeaderBoard
from statballerz.serializers import CentralSerializer, GoalKeeperSerializer, PlayerSerializer, PlayerLeaderBoardSerializer
##from django.contrib.auth.models import User


# Create your views here.

class CentralViewSet(viewsets.ModelViewSet):

    queryset = Central.objects.all()
    serializer_class = CentralSerializer

    # def central_list(request):
    #     if request.method == 'GET':
    #         queryset = Central.objects.all().order_by('instance')
    #         serializer = CentralSerializer(queryset, many = True)

    #     if request.method == 'POST':
    #         serializer = CentralSerializer(data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return response (serializer.data, status = status.HTTP_201_CREATED)





# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = userSerializers


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    


    # def player_list(request):
    #     if request.method == 'GET':
    #         queryset = Player.objects.all()
    #         serializer = PlayerSerializer(queryset, many=True)
    #         return response(serializer.data)

    #     if request.method == 'POST':
    #         serializer = PlayerSerializer(data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return response(serializer.data, status= status.HTTP_201_CREATED)






    

class PlayerLeaderBoardSet(viewsets.ModelViewSet):
    queryset = PlayerLeaderBoard.objects.all()
    serializer_class = PlayerLeaderBoardSerializer
    

    # def leaderboard_list(request):

        
    #     if request.method == 'GET':
    #         queryset = PlayerLeaderBoard.objects.all()
    #         serializer = PlayerLeaderBoardSerializer(queryset, many = True)
    #         return response(serializer.data)

        
    #     if request.method == 'POST':
    #         serializer = PlayerLeaderBoardSerializer(data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return response(serializer.data, status= status.HTTP_201_CREATED)


class GoalKeeperSet(viewsets.ModelViewSet):
    queryset = GoalKeeper.objects.all()
    serializer_class = GoalKeeperSerializer

    # def goalkeeper(request):
    #     if request.method == 'GET':
    #         queryset = GoalKeeper.object.all()
    #         serializer = GoalKeeperSerializer(queryset, many = True)
    #         return response(serializer.data)

    #     if request.method == 'POST':
    #         serializer = GoalKeeperSerializer(data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return response(serializer.data, status= status.HTTP_201_CREATED)