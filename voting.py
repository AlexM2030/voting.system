# Define 2 variables for each nominee running in the election
nominee1 = input('Enter nominee 1 name: ')
nominee2 = input('Enter nominee 2 name: ')

# Count the number of votes each nominee receives
nom_1_votes = 0
nom_2_votes = 0

# List of voter id participating in election and number of voters
voters_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_of_voter = len(voters_id)

# Program logic

while True:
    if voters_id == []:
        print('Voting session is over. ')
        if nom_1_votes > nom_2_votes:
            percent_win = (nom_1_votes / num_of_voter) * 100
            print(f'{nominee1} has won the election with {percent_win}% of votes! ')
            break
        elif nom_2_votes > nom_1_votes:
            percent_win = (nom_2_votes / num_of_voter) * 100
            print(f'{nominee2} has won the election with {percent_win}% of votes! ')
            break
    
    else:
        voter = int(input('Enter your voter id: '))
        if voter in voters_id:
            print('You are a registered voter. ')
            voters_id.remove(voter)
            vote_choice = int(input('Enter your preferred nominee 1 or 2: '))
            if vote_choice == 1:
                nom_1_votes += 1
                print('Thank you for casting your vote! ')
            elif vote_choice == 2:
                nom_2_votes += 1
                print('Thank you for casting your vote! ')
            else:
                print('You selection is not valid! ')
        else:
            print('You are not a registered voter or have already voted! ')



            