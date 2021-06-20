import random
while True:
    print("make your choice:")
    choice = input()
    choice = choice.lower()
    print("my choice is:", choice)
    
    choices = ['rock','paper','scissors']
    computerChoice = random.choice(choices)
    print("computer choice is:", computerChoice)
    
    choiceDict = {'rock': 0, 'paper': 1, 'scissors': 2}
    
    
    choiceIndex = choiceDict.get(choice,3)
    computerIndex = choiceDict.get(computerChoice)
    
    resultMatrix = [[0,2,1],
                    [1,0,2],
                    [2,1,0],
                    [3,3,3]
                    ]
    resultIdx= resultMatrix[choiceIndex][computerIndex]
    resultMessage = ['it is a tie','you win','you lose','invalid choicerock']
    result = resultMessage[resultIdx]
    print(result)
    print()