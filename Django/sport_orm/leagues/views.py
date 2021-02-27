from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		"ligas_biesbol": League.objects.filter(sport="Baseball"),
		"ligas_mujeres": League.objects.filter(name__contains="Women"),
		"tipo_hockey": League.objects.filter(name__contains="Hockey"),
		"no_futbol": League.objects.exclude(sport="Football") & League.objects.exclude(sport="Soccer"),
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
		
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")