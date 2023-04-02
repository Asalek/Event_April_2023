<?php

while(1)
{
	echo "Choose rock, paper, or scissors: ";

	$choice = trim(fgets(STDIN));
	// $choice = trim($choice);

	$random_nb = mt_rand(0, 2);

	$game_choice = array( "rock", "scissors" , "paper");

	$index = array_search($choice, $game_choice);

	if($index === false){
		echo "\033[35merror choice: $choice not found !\033[0m\n";
	}
	else
	{
		if ($index == $random_nb)
			echo "\033[33mdraw we both choose : $game_choice[$index]\033[0m\n";
		else if ($game_choice[$index] == "rock" && $game_choice[$random_nb] == "scissors"
			|| $game_choice[$index] == "paper" && $game_choice[$random_nb] == "rock"
			|| $game_choice[$index] == "scissors" && $game_choice[$random_nb] == "paper")
			echo "\033[32mCongratulations! You won! The computer chose: $game_choice[$random_nb]\033[0m\n";
		else
			echo "\033[31mSorry, you lost. The computer chose $game_choice[$random_nb].\033[0m\n";
	}
}
?>
