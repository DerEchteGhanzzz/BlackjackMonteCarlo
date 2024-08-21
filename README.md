# Strategy
We have 2 strategies. Safe and Not Safe. These go into effect whenever the dealer has a bad card (lower than 7) or a good card (everything else) (aces count as 11 in this sense). 
We loop through all possible targets from 2, 2 to 21, 21 and perform 100_000 rounds with these targets. We stop playing a round whenever we reach the current target (depending on the single card that the house has).
Each game we bet 1 kr. (we couldn't find a euro sign and we didn't have the internet to search for one on the ColorLine, so we did it in Norse Kroner like the casino on the boat)

You can also do these calculations. We have written them very inefficiently, so it takes about 5 minutes.

glhf!
