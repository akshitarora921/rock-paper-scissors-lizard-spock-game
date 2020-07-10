import random
class game:
    def __init__(self):
        self.user=0
        self.computer = 0
    # print Rules
    def rules():
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
    def user_input(self):
        # user input
        print('''
        1. Rock
        2. Paper
        3. Scissor
        4. Lizard
        5. Spock

        ''')
        self.user = int(input())
        if self.user<1 and self.user>5:
            print('wrong input')
        elif self.user ==1:
            print('user choose Rock')
        elif self.user ==2:
            print('user choose Paper')
        elif self.user ==3:
            print('user choose Scissor')
        elif self.user ==4:
            print('user choose Lizard')
        elif self.user ==5:
            print('user choose Spock')


    def computer_input(self):
        self.computer = random.randint(1,5)
        if self.computer ==1:
            print('computer choose Rock')
        elif self.computer ==2:
            print('computer choose Paper')
        elif self.computer ==3:
            print('computer choose Scissor')
        elif self.computer ==4:
            print('computer choose Lizard')
        elif self.computer ==5:
            print('computer choose Spock')

    def game(self):
        print('')   
        if self.user== self.computer:
            print("Its a tie!!")
        # When user wins
        # Rock
        elif self.user==1 and (self.computer==3 or self.computer==4):
            print('user wins!!')
            if self.computer == 3:
                print('Rock crushes Scissor')
            else:
                print('Rock crushes Lizard')
        # paper
        elif self.user==2 and (self.computer==1 or self.computer==5):
            print('user wins!!')
            if self.computer == 1:
                print('Paper cover Rock')
            else:
                print('Paper disprove Spock')
        # Scissor
        elif self.user==3 and (self.computer==2 or self.computer==4):
            print('user wins!!')
            if self.computer == 2:
                print('Scissor cut Paper')
            else:
                print('Scissor dispicate Lizard')
        # Lizard
        elif self.user==4 and (self.computer==2 or self.computer==5):
            print('user wins!!')
            if self.computer == 2:
                print('Lizard eat Paper')
            else:
                print('Lizard poisons Spock')
        # Spock
        elif self.user==5 and (self.computer==1 or self.computer==3):
            print('user wins!!')
            if self.computer == 1:
                print('Spock vapoures Rock')
            else:
                print('Spock smashes Scissor')
        
        # When self.computer wins
        # Rock
        elif self.computer==1 and (self.user==3 or self.user==4):
            print('computer wins!!')
            if self.user == 3:
                print('Rock crushes Scissor')
            else:
                print('Rock crushes Lizard')
        # paper
        elif self.computer==2 and (self.user==1 or self.user==5):
            print('computer wins!!')
            if self.user == 1:
                print('Paper cover Rock')
            else:
                print('Paper disprove Spock')
        # Scissor
        elif self.computer==3 and (self.user==2 or self.user==4):
            print('computer wins!!')
            if self.user == 2:
                print('Scissor cut Paper')
            else:
                print('Scissor dispicate Lizard')
        # Lizard
        elif self.computer==4 and (self.user==2 or self.user==5):
            print('computer wins!!')
            if self.user == 2:
                print('Lizard eat Paper')
            else:
                print('Lizard poisons Spock')
        # Spock
        elif self.computer==5 and (self.user==1 or self.user==3):
            print('computer wins!!')
            if self.user == 1:
                print('Spock vapoures Rock')
            else:
                print('Spock smashes Scissor')
                
class main():
    g= game()
    while(True):
        g.user_input()
        g.computer_input()
        g.game()

