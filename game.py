import random
# print Rules
print('''
1. Scissors cuts Paper
2. Paper covers Rock
3. Rock crushes Lizard
4. Lizard poisons Spock
5. Spock smashes Scissors
6. Scissors decapitates Lizard
7. Lizard eats Paper
8. Paper disproves Spock
9. Spock vaporizes Rock
10. Rock crushes Scissors''')
# user input
print('''
1. Rock
2. Paper
3. Scissor
4. Lizard
5. Spock

''')
user = int(input())
if user<1 and user>5:
    print('wrong input')
elif user ==1:
    print('user choose Rock')
elif user ==2:
    print('user choose Paper')
elif user ==3:
    print('user choose Scissor')
elif user ==4:
    print('user choose Lizard')
elif user ==5:
    print('user choose Spock')
print('')

computer = random.randint(1,5)
if computer ==1:
    print('computer choose Rock')
elif computer ==2:
    print('computer choose Paper')
elif computer ==3:
    print('computer choose Scissor')
elif computer ==4:
    print('computer choose Lizard')
elif computer ==5:
    print('computer choose Spock')
4

