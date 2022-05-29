#Solution for Question 10- A
import collections

# Referred from https://github.com/Schachte/stable-matching-algorithm
#Super group 1 teams
rankings_Super_Group_1 = {
    'A': 	['D', 'F', 'E'],
    'B': 	['E', 'D', 'F'],
    'C': 	['E', 'F', 'D']

}

#Super group 2 teams
rankings_Super_Group_2 = {
    'D': 	['A', 'C', 'B'],
    'E': 	['C', 'A', 'B'],
    'F':  	['A', 'B', 'C']

}

#variable to store temporary matches
match = []
#team without opponents
team_wo_opponent = []

def stable_matching(team):
    #Locate first available opponent
        
    print("Current team "+team)
    for opp in rankings_Super_Group_1[team]:
        matched_team=[]
              
        for teams in match:
            if opp in teams:
                matched_team = teams
      
        if (len(matched_team) == 0):
            #match the team and opp
            match.append([team, opp])
            team_wo_opponent.remove(team)           
            break
        #team already matched
        elif (len(matched_team) > 0):            
            #Check preference
            new_opp = rankings_Super_Group_2[opp].index(team)
            crnt_opp = rankings_Super_Group_2[opp].index(matched_team[0][0])

            if (crnt_opp > new_opp):                                                
                #new opponent is added
                team_wo_opponent.append(matched_team[0][0])
                #old team is removed
                team_wo_opponent.remove(team)
                matched_team[0][0] = team
                break

def main():
    #Get teams initially
    for team in rankings_Super_Group_1:
        team_wo_opponent.append(team)

    print(team_wo_opponent)
    #Match until all teams are matched with opponents
    while (len(team_wo_opponent) > 0):
        for team in team_wo_opponent:
            stable_matching(team)
    print('Stable match output::::: \n')
    print(match)
main()

