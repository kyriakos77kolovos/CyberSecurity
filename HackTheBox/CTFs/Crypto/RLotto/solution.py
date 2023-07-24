import time
import random

seed = int(input("Enter the timestamp (enter 0 if not aware) :"))

if seed == 0:
    seed = int(time.time()) - 2_500_500 #2_500_500 10 sec
if seed == 1:
    seed = int(time.time()) - 15_000_000

winning_numbers = list(int(x) for x in input("Enter extracted numbers from the rlotto program: ").split(" "))

print("starred seed: ", seed)

while True:
    random.seed(seed)
    extracted = []
    for item in winning_numbers:
        r = random.randint(1,90)
        if item != r:
            seed +=1 
            break
        else:
            extracted.append(r)
    if len(extracted) == 5:
        break

print("Found seed: ", seed)

solution = ""
next_five = []

while(len(next_five)<5):
    r = random.randint(1,90)
    if (r not in next_five):
        next_five.append(r)
        solution += str(r) + " "
solution = solution.strip()
print("\nsolution: " , solution)