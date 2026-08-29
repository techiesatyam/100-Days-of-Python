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

# Command line arguments
import sys

if len(sys.argv) < 2:
    sys.exit("*minimum 4 letters required")
for en in sys.argv:
    print(f"Hello, my name is {en}")

print("Hello, my name is ", sys.argv[1])