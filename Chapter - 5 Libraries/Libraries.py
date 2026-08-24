import random 

# Function for choosing 
choose = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
print(choose)

# Function for selecting number randomly
choice = random.randint(1, 5)
print(choice)

#Function for shuffling the 
rome = ["!", "@", "#", "$", "^", "<>"]
random.shuffle(rome)
for ro in rome:
    print(ro)

import statistics

mean = statistics.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(mean)

mode = statistics.mode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(mode)