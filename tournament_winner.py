def tournamentWinner(competitions, results):
    
    teams = {}

    for i in range(len(competitions)):
        
        if results[i] == 0:
            winningTeam = competitions[i][1]
        else:
            winningTeam = competitions[i][0]
        
        if winningTeam in teams.keys():
             teams[winningTeam] += 3
        else:
             teams[winningTeam] = 0
             teams[winningTeam] += 3
            
    
    print(teams)
    max = 0 
    winnerTeam = ''
    for i in teams.keys():
        if max < teams[i]:
            max = teams[i]
            winnerTeam = i
    return winnerTeam