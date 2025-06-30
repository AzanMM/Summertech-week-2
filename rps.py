from random import randint
while True:
    comp_guess=randint(0,2)
    player_guess=input('0. Rock 1. Paper 2. Scissors? 3. Exit ')
    if player_guess=="3":
        break
    
    if comp_guess==int(player_guess):
        print('You both threw the same thing please try again')
    elif comp_guess==0 and int(player_guess)==1:
        print('user has won the round computer threw up rock and user has throwm up paper ')
    elif comp_guess==0 and int(player_guess)==2:
        print('Computer has won the round user threw up scissors amd the computer had thrown up rock ')
    elif comp_guess==1 and int(player_guess)==0:
        print('Computer has won the round user threw up rock while the computer threw up paper')
    elif comp_guess==1 and int(player_guess)==2:
        print('user has won the round computer threw up paper while the user threw up scisscors ')
    elif comp_guess==2 and int(player_guess)==0:
        print('user has won the round computer threw up scissors and user has throwm up rock ')
    elif comp_guess==2 and int(player_guess)==1:
        print('Computer has won the round user threw up paper amd the computer had thrown up scissors ')
    else:
        print('invalid input try again')