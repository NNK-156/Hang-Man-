
import random
from Words_list import words
randomChoice = random.choice(list(words))
while ' ' in randomChoice:
    randomChoice = random.choice(list(words))

def check(word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            return True
    return False

    

# print(randomChoice)
print('The word you need to guess is: ')
quest = '⭐'* len(randomChoice)
print(quest)

tries = 10
count = 0
idxList = []
for k in range(tries):
    playerChoice = input('Your guess is: ').lower()
    if check(randomChoice,playerChoice):
        
        for times in range(len(randomChoice)):
            if playerChoice == randomChoice[times]:
                idxList.append(times)
        # print(idxList)
        quest = list(quest)
        for value in idxList:
            quest[value] = playerChoice 
        quest = ''.join(quest)
        idxList = []
        count += 1
    else:
        print(f'Nope! There is no \"{playerChoice}\" in the word!')
        count += 1
    if quest == randomChoice:
        print('You did it! Nice!')
        break
    print(quest + '\n')      
    if tries - count <= 0:
        print(f'The answer is \"{randomChoice}\"!')
        print('You lost, nigga!')
        break
    else:
        print(f'You have {tries - count} tries left! ')
