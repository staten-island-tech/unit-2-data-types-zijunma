def calculate_remaining_hunger(initial_hungerpoints, seconds_waited, apples_eaten, hunger_gainedperapple, hunger_lostpersecond):

# calc total number of hunger gained from eating apples

totalhungerpointsgained = apples_eaten * initial_hungerpoints

# calculate the hunger points lost when waiting
 
total_hunger_points_lost = hunger_lostpersecond * seconds_waited

# calculate the final hunger level

final_hunger = totalhungerpointsgained - total_hunger_points_lost

hunger_lostpersecond = int(input())
initial_hungerpoints = int(input())
seconds_waited = int(input())
apples_eaten = int(input())