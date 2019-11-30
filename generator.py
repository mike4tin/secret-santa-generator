import math
import random

group_a = ["Kari", "Tom", "Jake", "Madison"]
group_b = ["Todd", "Brett", "Miranda", "Greg"]
group_c = ["Wendy", "Mike Senior", "Mike", "Andrew", "Brianne"]
group_d = ["Grandma", "Chuck"]

selected = []
selections = []

a_possibilities = group_b + group_c + group_d
for person in group_a:
    finished = False
    while not finished:
        selection = random.choice(a_possibilities)
        if selection not in selected:
            finished = True
            selected.append(selection)
            selections.append((person, selection))

#print(selections)

b_possibilities = group_a + group_c + group_d
for person in group_b:
    finished = False
    while not finished:
        selection = random.choice(b_possibilities)
        if selection not in selected:
            finished = True
            selected.append(selection)
            selections.append((person, selection))
#print(selections)

c_possibilities = group_a + group_b + group_d
for person in group_c:
    finished = False
    while not finished:
        selection = random.choice(c_possibilities)
        if selection not in selected:
            finished = True
            selected.append(selection)
            selections.append((person, selection))
#print(selections)

d_possibilities = group_a + group_b + group_c
for person in group_d:
    finished = False
    while not finished:
        selection = random.choice(d_possibilities)
        if selection not in selected:
            finished = True
            selected.append(selection)
            selections.append((person, selection))
#print(selections)

output = open("selections.txt", "w")
mikes_output = open("mikes_selection.txt", "w")

if len(selected) == len(group_a + group_b + group_c + group_d):
    print("All selections have been made! Please check the output file for results!")
    output.write("Secret Santa 2019\n")
    mikes_output.write("Mikes Secret Santa 2019\n")
else:
    exit(0)

for person, selection in selections:
    if selection is "Mike":
        mikes_output.write(person + " --> " + selection)
    else:
        output.write(person + " --> " + selection)
        output.write("\n")






