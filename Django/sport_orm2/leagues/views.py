from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		"ligas_biesbol": League.objects.filter(sport="Baseball"),
		"ligas_mujeres": League.objects.filter(name__contains="Women"),
		"tipo_hockey": League.objects.filter(name__contains="Hockey"),
		"no_futbol": League.objects.exclude(sport="Football"),
		"ligas_conferencias": League.objects.filter(name__contains="conference"),
		"ligas_region_atlantica": League.objects.filter(name__contains="Atlantic"),
		"teams_Dallas": Team.objects.filter(location="Dallas"),
		"teams_Raptors": Team.objects.filter(team_name__contains="Raptors"),
		"teams_city": Team.objects.filter(location__contains="City"),
		"teams_t": Team.objects.filter(team_name__startswith="T"),
		"teams_az": Team.objects.order_by("location"),
		"teams_za": Team.objects.order_by("-team_name"),
		"player_Cooper": Player.objects.filter(last_name="Cooper"),
		"player_Joshua": Player.objects.filter(first_name="Joshua"),
		"player_joshua_no_cooper": Player.objects.filter(first_name="Joshua").exclude(last_name="Cooper"),
		"player_Alexander_Wyatt": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
		"teams_Atlantic_soccer": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"player_penguins": Player.objects.filter(curr_team__team_name='Penguins'),
		"Iplayers": Player.objects.filter(curr_team__league_id=2),
		"Lplayers": Player.objects.filter(curr_team__league_id=7) & Player.objects.filter(last_name="Lopez"),
		"fplayers": Player.objects.filter(curr_team__league_id=7) | Player.objects.filter(curr_team__league_id=9),
		'fteams': Team.objects.filter(league__sport="Football"),
		'steams': Team.objects.filter(all_players__first_name="Sophia"),
		'sleague': League.objects.filter(teams__id=25) | League.objects.filter(teams__id=4) | League.objects.filter(
			teams__id=32),
		"notfplayers": Player.objects.filter(last_name='Flores') & Player.objects.filter(~Q(curr_team_id=10)),
		'seteams': Team.objects.filter(all_players__id=115),
		"maniplayers": Player.objects.filter(all_teams__id=4),
		"vikiplayers": Player.objects.filter(all_teams__id=40),
		'jacteams': Team.objects.filter(all_players__id=151)[:3],
		"atplayers": Player.objects.filter(first_name="Joshua") & Player.objects.filter(all_teams__league_id=3),
		"playerNums": Team.objects.annotate(nplayer=Count('all_players')).filter(nplayer__gt=12),
		"allplayerteam": Team.objects.annotate(nplayer=Count('all_players')).order_by('nplayer')
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")