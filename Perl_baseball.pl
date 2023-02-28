#!/usr/bin/perl 

use warnings;
use strict;
use File::Basename;

# Importing and organizing baseball data for National League for years 2017 - 2021

my $filename2 = </mnt/c/Users/HC/Desktop/Baseball_Data/baseball_test_two.csv>;

#delete the output file if it alredy exists to start fresh each time this program is run
if (-e $filename2){ unlink $filename2 or die "error in delete";}


open (FH2, '>', $filename2) or die $!;
#print FH2 "Team,Season,Games_Played,Home_Played,Home_Won,Home_Lost,Away_Played,Away_Won,Away_Lost,H_Runs,H_Runs_Allowed,A_Runs,A_Runs_Allowed\n";

my @file_directory =</mnt/c/Users/HC/Desktop/Baseball_Data/BBDIR/*>;
foreach my $filename (@file_directory){
	#print $filename . "\n";
	my $just_filename = basename($filename);
	$_ = $just_filename;
	/_/;
	my $just_filename_year = $';
	$_ = $just_filename_year;
	/\./;
	$just_filename_year = $`;


open (FH, '<', $filename) or die $!;
open (FH2, '>>', $filename2) or die $!;

my $sum_team_home = 0;
my $sum_opponent_home = 0;
my $sum_team_away = 0;
my $sum_opponent_away = 0;
my $home_game_won = 0;
my $home_game_lost = 0;
my $home_games_played = 0;
my $away_game_won = 0;
my $away_game_lost = 0;
my $away_games_played = 0;
my $team_name = 0;
my $games_played_count = 0;




#read just the first line because it is headers
my $firstline = <FH>;

while(my $line = <FH>){
	$games_played_count++;
	chomp $line;
       
        my @team_field = split "," , $line;	
	#my $team_name = $team_field[3];


	if ($line !~ /@/){
        	my @fields = split "," , $line;
                $team_name = $fields[3];
		$home_games_played++;
        	$sum_team_home += $fields[7];
        	$sum_opponent_home += $fields[8];
		if ($fields[6] =~ 'W'){
			$home_game_won++;
		}
		if ($fields[6] =~ 'L'){
			$home_game_lost++;
		}
}

	if ($line =~ /@/){
        	my @fields = split "," , $line;
                $team_name = $fields[3];
		$away_games_played++;
        	$sum_team_away += $fields[7];
        	$sum_opponent_away += $fields[8];
		if ($fields[6] =~ 'W'){
			$away_game_won++;
		}
		if ($fields[6] =~ 'L'){
			$away_game_lost++;
		}
}

}

print FH2 "$team_name,";
print FH2 "$just_filename_year,";
print FH2 "$games_played_count,";
print FH2 "$home_games_played,";
print FH2 "$home_game_won,";
print FH2 "$home_game_lost,";
print FH2 "$away_games_played,";
print FH2 "$away_game_won,";
print FH2 "$away_game_lost,";
print FH2 "$sum_team_home,";
print FH2 "$sum_opponent_home,";
print FH2 "$sum_team_away,";
print FH2 "$sum_opponent_away";
print FH2 "\n";
close(FH);
} # close foreach loop for BBDIR
close(FH);
close(FH2);


