import numpy as np


def minmax(tableA, tableB):
    
    #sortedA = list(range(tableA.shape[0]))
    #sortedB = list(range(tableB.shape[1]))
    #sortedA.sort(key=lambda var: tableA[var,:].min(), reverse=True)
    #sortedB.sort(key=lambda var: tableB[:,var].min(), reverse=True)

    sortedA  = [np.array(tableA[k,:]).min() for k in range(tableA.shape[1])]
    sortedB  = [np.array(tableB[:,k]).min() for k in range(tableB.shape[0])]

    a = np.where(sortedA == max(sortedA))
    b = np.where(sortedB == max(sortedB))

    return [a, b]


def nasheq(tableA, tableB):
    bType = False

    aStrategies = []
    for i in range(tableA.shape[1]):
        aStrategies.append((np.argmax(tableA[:,i]), i))

    bStrategies = []
    for i in range(tableB.shape[0]):
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
            if tableA[strat1[0], strat1[1]] > tableA[strat2[0], strat2[1]] and tableB[strat1[0], strat1[1]] > tableB[strat2[0], strat2[1]]:
                bAllFeasible = False
                feasibleStategies.append(strat1)
    
    if bAllFeasible:
        feasibleStategies = nashStrategies

    return feasibleStategies


def vonStack(tableA, tableB):
    followerStrat = []
    for i in range(tableB.shape[0]):
        max_elements = np.where(tableB[i, :].max() == tableB[i, :])[1]
        followerStrat.append(max_elements)

    leaderStrat = list(range(tableA.shape[1]))
    leaderStrat.sort(key=lambda var: tableA[var, followerStrat[var].min()], reverse=True)

    minimal_values = [tableA[i, :].min() for i in range(tableA.shape[1])]
    print(minimal_values)
    indexes = np.where(max(minimal_values) == minimal_values)
    print(indexes)
    print(leaderStrat)

    strategy = (indexes[0], followerStrat[leaderStrat[0]])
    return strategy

    
if __name__ == '__main__':   

    gameOneA = np.matrix([[2, 5, 0], [4, -5, -8], [1, 3, 0]])
    gameOneB = np.matrix([[-1, 4, 1], [6, -8, 1], [2, 0, -7]])
    gameTwoA = np.matrix([[5, 3, -1], [-3, -5, 8], [1, 2, -1]])
    gameTwoB = np.matrix([[-1, 4, 4], [5, -8, 5], [-6, 1, 1]])

    result = minmax(gameOneA, gameOneB)
    print('MINMAX:')
    for i in result[0][0]:
        for j in result[1][0]:
            print(f"Coordinates {i + 1}, {j + 1}, game value: {gameOneA[i, j]}, {gameOneB[i, j]}")

    nash_result = nasheq(gameOneA, gameOneB)

    print('\nNash:')
    
    for solution in nash_result:
        print(f"Coordinates: {solution[0] + 1}, {solution[1] + 1}, game value: {gameOneA[solution[0], solution[1]]}, {gameOneB[solution[0], solution[1]]}")

    von_result = vonStack(gameTwoA, gameTwoB)

    print('\nvon Steckelberg')
    for i in von_result[0]:
        for j in von_result[1]:
            print(f"Coordinates {i + 1}, {j + 1}, game value: {gameTwoA[i, j]}, {gameTwoB[i, j]}")


