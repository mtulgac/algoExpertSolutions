def tournamentWinner(competitions, results):
    # Write your code here.
    teamList = []
    for j in range(len(competitions)):
        for k in range(2):
            if competitions[j][k] in teamList:
                pass
            else:
                teamList.append(competitions[j][k])

    points = {}
    for t in teamList:
        points[t] = 0

    for i in range(len(results)):
        if results[i] == 0:
            points[competitions[i][1]] +=3
        else:
            points[competitions[i][0]] +=3

    max_key = max(points, key=points.get)
    return max_key
