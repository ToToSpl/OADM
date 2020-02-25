    #gameA = np.matrix([[2,30],[0,8]])
    #gameB = np.matrix([[2,0],[30,8]])

    #gameA = np.matrix([[-2,1],[1,-1]])
    #gameB = np.matrix([[-1,1],[1,-2]])

    #gameA = np.matrix([[0,2,1.5],[1,1,3],[-1,2,2]])
    #gameB = np.matrix([[-1,1,-0.75],[2,0,1],[0,1,-0.5]])

    #gameA = np.matrix([[15, 0], [30, -15]])
    #gameB = np.matrix([[20, 30], [10, 0]]) 



def nasheq(tableA, tableB, tableType='costs'):
    bType = True
    if tableType == 'payoff':
        bType = False

    aStrategies = []
    for i in range(tableA.shape[1]):
        if bType:
            aStrategies.append((np.argmin(tableA[:,i]), i))
        else:
            aStrategies.append((np.argmax(tableA[:,i]), i))

    bStrategies = []
    for i in range(tableB.shape[0]):
        if bType:
            bStrategies.append((i, np.argmin(tableB[i,:])))
        else:
            bStrategies.append((i, np.argmax(tableB[i,:])))

    nashStrategies = []
    for i in range(len(aStrategies)):
        for j in range(len(bStrategies)):
            if aStrategies[i] == bStrategies[j]:
                nashStrategies.append(aStrategies[i])

    feasibleStategies = []
    bAllFeasible = True
    for strat1 in nashStrategies:
        for strat2 in nashStrategies:
            if bType:
                if tableA[strat1[0], strat1[1]] < tableA[strat2[0], strat2[1]] and tableB[strat1[0], strat1[1]] < tableB[strat2[0], strat2[1]]:
                    bAllFeasible = False
                    feasibleStategies.append(strat1)
            else:
                if tableA[strat1[0], strat1[1]] > tableA[strat2[0], strat2[1]] and tableB[strat1[0], strat1[1]] > tableB[strat2[0], strat2[1]]:
                    bAllFeasible = False
                    feasibleStategies.append(strat1)
    
    if bAllFeasible:
        feasibleStategies = nashStrategies
    print("Nash strategies:")
    print(nashStrategies)
    print("Feasible strategies:")
    print(feasibleStategies)
    return feasibleStategies


#leader is in y axis d1 player
def vonStack(tableA, tableB, tableType='costs'):
    bType = True
    if tableType == 'payoff':
        bType = False

    followerStrat = []
    for i in range(tableA.shape[0]):
        if bType:
            followerStrat.append(np.argmin(tableB[i,:]))
        else:
            followerStrat.append(np.argmax(tableB[i,:]))

    leaderStrat = list(range(tableA.shape[0]))
    if bType:
        leaderStrat.sort(key=lambda var: tableA[var, followerStrat[var]], reverse=False)
    else:
        leaderStrat.sort(key=lambda var: tableA[var, followerStrat[var]], reverse=True)

    strategy = (leaderStrat[0], followerStrat[leaderStrat[0]])
    print(strategy)
    return strategy



#print('\nNASH EQUATIONS:')
#nasheq(gameOneA, gameOneB)

print('\nVON STACKELBERG:')
vonStack(gameTwoA, gameTwoA)