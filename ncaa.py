from sportsipy.ncaab.roster import Roster
from sportsipy.ncaab.teams import Teams
import csv

teams = Teams(2014)
with open('2014stats.csv', 'w', newline='') as f:
	thewriter = csv.writer(f)
	thewriter.writerow(['Name', 'Points','Assist%','Assists', 'block %', 'blocks', 'def rebounds %', 'def rebounds', 'EFG%', 'FGA', 'FG%', 'FG', 'FTA%', 'FTAs', 'FT%','FTs', 'Minutes', 'Off Rebounds%', 'Off Rebounds', 'Fouls', 'Steal%', 'Steals', '3s attempt%', '3s attempts', '3s %', '3s', 'total rebounds%', 'total rebounds', 'true shooting%', 'turnover%', 'turnovers', '2s attempts', '2s %', '2s', 'usage'])
	for team in teams:
	     print(team.name, team.abbreviation)
	     name = Roster(team.abbreviation, year = '2014')

	     for player in name.players:
	        print(player.name, "Points:", player.points, "Assist Percentage", player.assist_percentage, "Assists:", player.assists, "FGA", player.field_goal_attempts)
	        thewriter.writerow([player.name, player.points, player.assist_percentage, player.assists, player.block_percentage, player.blocks, player.defensive_rebound_percentage, player.defensive_rebounds, player.effective_field_goal_percentage, player.field_goal_attempts, player.field_goal_percentage, player.field_goals, player.free_throw_attempt_rate, player.free_throw_attempts, player.free_throw_percentage, player.free_throws, player.minutes_played, player.offensive_rebound_percentage, player.offensive_rebounds, player.personal_fouls, player.steal_percentage, player.steals, player.three_point_attempt_rate, player.three_point_attempts, player.three_point_percentage, player.three_pointers, player.total_rebound_percentage, player.total_rebounds, player.true_shooting_percentage, player.turnover_percentage, player.turnovers, player.two_point_attempts, player.two_point_percentage, player.two_pointers, player.usage_percentage])













