def calculate_remaining_hunger(initial_hunger_points, apples_eaten, hunger_gained_per_apple, hunger_lost_per_second, waiting_seconds):

# calc total number of hunger gained from eating apples

    total_hunger_points_gained = apples_eaten * initial_hunger_points

# makes sure the hunger doesn't overflow the max hunger bar
    
    total_hunger_points_gained = min(total_hunger_points_gained, max_hunger_points - initial_hunger_points)
 
# calculate the hunger points lost when waiting
 
    total_hunger_points_lost = hunger_lost_per_second * waiting_seconds

# calculating the final hunger level

    remaining_hunger_points = max(0, initial_hunger_points + total_hunger_points_gained - total_hunger_points_lost)

    return remaining_hunger_points

max_hunger_points = (100)
initial_hunger_points = int(input("Initial Hunger Points:"))
apples_eaten = int(input("Apples Eaten:"))
hunger_gained_per_apple = (1)
hunger_lost_per_second = (1)
waiting_seconds = int(input("Seconds Waiting:"))
 
result = calculate_remaining_hunger(initial_hunger_points, apples_eaten, hunger_gained_per_apple, hunger_lost_per_second, waiting_seconds)
print("Bob's remaining hunger points:", result)

# alternative user input for setting it up 
""" int(input("Hunger Lost Per Second Waiting:"))
int(input("Max Hunger Points:"))
int(input("Hunger Gained Per Apple:")) """