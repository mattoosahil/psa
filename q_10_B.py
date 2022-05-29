#Solution for Question 10- B
import collections
import time
import random

# Referred from https://github.com/Schachte/stable-matching-algorithm
#Super group 1 teams
l1= ['D', 'F', 'E']
l2= ['E', 'D', 'F']
l3= ['E', 'F', 'D']
l4= ['A', 'C', 'B']
l5= ['C', 'A', 'B']
l6= ['A', 'B', 'C']

num=10


def shuffle_input():
    for i in range(1000):
        random.shuffle(l1)
        random.shuffle(l2)
        random.shuffle(l3)
        random.shuffle(l4)
        random.shuffle(l5)
        random.shuffle(l6)
        rankings_Super_Group_1 = {
            'A': 	l1,
            'B': 	l2,
            'C': 	l3
        }
        rankings_Super_Group_2 = {
            'D': 	l4,
            'E': 	l5,
            'F': 	l6
        }
def stable_matching(team,rankings_Super_Group_1,rankings_Super_Group_2, match, team_wo_opponent, total, swap ):
    #Locate first available opponent
        
    #print("Current team "+team)
    for opp in rankings_Super_Group_1[team]:
        matched_team=[]
              
        for teams in match:
            if opp in teams:
                matched_team = teams
                #print('matched team:')
                #print(matched_team)
                #print(matched_team[0][0])
      
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
                y = list(matched_team)
                y[0] = team
                matched_team = tuple(y)
                
                break
    
def cal_per(tot):
    percent= tot/num
    percent=percent*100
    print('Output percentage=')
    print(percent)
def main():
    total_count=0
    swaps=0
    for i in range(num):
        random.shuffle(l1)
        random.shuffle(l2)
        random.shuffle(l3)
        random.shuffle(l4)
        random.shuffle(l5)
        random.shuffle(l6)
        rankings_Super_Group_1 = {
            'A': 	l1,
            'B': 	l2,
            'C': 	l3
        }
        rankings_Super_Group_2 = {
            'D': 	l4,
            'E': 	l5,
            'F': 	l6
        }
        #variable to store temporary matches
        match = []
        #team without opponents
        team_wo_opponent = []
        #Get teams initially
        for team in rankings_Super_Group_1:
            team_wo_opponent.append(team)

        #print(team_wo_opponent)
        #Match until all teams are matched with opponents
        while (len(team_wo_opponent) > 0):
            for team in team_wo_opponent:
                stable_matching(team, rankings_Super_Group_1, rankings_Super_Group_2, match, team_wo_opponent, total_count, swaps )
                
                
        #print('Stable match output::::: \n')
        #print(match)
        #print(len(match))
        if(len(match) == 3):
            total_count+=1


    cal_per(total_count)
start_time = time.time()    
main()
print("Execution time: %s seconds" % (time.time() - start_time))
