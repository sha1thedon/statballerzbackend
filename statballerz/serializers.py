from rest_framework import serializers
from statballerz.models import Central, GoalKeeper, Player, PlayerLeaderBoard
##from django.contrib.auth.models import User

class CentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Central
        fields = '__all__'


# class userSerializers(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerLeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerLeaderBoard
        fields = '__all__'


class GoalKeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalKeeper
        fields = '__all__'