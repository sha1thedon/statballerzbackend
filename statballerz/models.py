from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Central(models.Model):
    instance = models.CharField(max_length=8, default="", primary_key=True)
    user_id = models.CharField(max_length=8, default="")
    team_id = models.CharField(max_length=8, default="")
    team_name = models.CharField(max_length=50, default="")
    player_id = models.CharField(max_length=8, default="")
    player_name = models.CharField(max_length=50, default="")
    goals = models.IntegerField(default=0)



class Player(models.Model):
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default =0)
    passes = models.IntegerField(default =0)
    key_passes = models.IntegerField(default =0)
    tackles = models.IntegerField(default =0)
    succ_dribbles = models.IntegerField(default =0)
    unsucc_dribbles = models.IntegerField(default =0)
    fouls = models.IntegerField(default =0)
    shot_target = models.IntegerField(default =0)
    shot_offtarget = models.IntegerField(default =0)
    lost_balls = models.IntegerField(default =0)


class PlayerLeaderBoard(models.Model):
    player_name = models.CharField(max_length=50, default="")
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default =0)
    passes = models.IntegerField(default =0)
    key_passes = models.IntegerField(default =0)
    tackles = models.IntegerField(default =0)
    succ_dribbles = models.IntegerField(default =0)
    unsucc_dribbles = models.IntegerField(default =0)
    fouls = models.IntegerField(default =0)
    shot_target = models.IntegerField(default =0)
    shot_offtarget = models.IntegerField(default =0)
    lost_balls = models.IntegerField(default =0)
    points = models.IntegerField(default = 0)
    minutesplayed = models.IntegerField(default =0 )


class GoalKeeper(models.Model):
     player_name = models.CharField(max_length=50, default="")
     saves = models.IntegerField(default =0)
     conceded = models.IntegerField(default =0)
     shots_faced = models.IntegerField(default =0)
     save_percentage = models.IntegerField(default =0)
     clean_sheets = models.IntegerField(default =0)
     one_v_one_won = models.IntegerField(default =0)
     one_v_one_lost = models.IntegerField(default =0)
     penalty_saves = models.IntegerField(default =0)
     penalty_conceded = models.IntegerField(default =0)
     unforced_errors = models.IntegerField(default =0)
     points = models.IntegerField(default =0)
     minutes_played = models.IntegerField(default =0)
     points_per_minute = models.IntegerField(default =0)


