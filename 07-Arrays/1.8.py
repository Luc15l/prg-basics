
computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
number = 0
computer_games = sorted(computer_games)
while len(computer_games) > number:
    print((number+1),computer_games[number])
    number +=1