def league_points(wins, draws, losses):
    
    wins = wins * 3
    
    draws = draws * 1
    
    losses = losses * 0
    
    total = wins + draws + losses
    return total
    
print(league_points(5, 0, 2))
    
