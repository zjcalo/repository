from random import randint
import random

answer_list = []

global our_list
our_list = ['1', '2', '3', '4', '5']

global our_list_pairs
our_list_pairs = {
'1':"One", 
'2':"Two", 
'3':"Three", 
'4':"Four", 
'5':"Five"
}







# Create a random integer that is one less
# than the length of our list

global rando
rando = randint(0, len(our_list)-1)


# choose a random index value from our list

answer = our_list[rando]


count = 1
while count < 4:
    rando = randint(0, len(our_list)-1)
    
    # if first selection, this is our answer
    
    if count == 1:
        answer = our_list[rando]
    
    # add the selection to our answer list    
    answer_list.append(our_list[rando])

    # remove answer from original list
    our_list.remove(our_list[rando])

    # then shuffle the list
    random.shuffle(our_list)

    # add one to the count
    count +=1


print(answer_list)
print(answer)

'''
# add the answer to our list of possible answers for the question

answer_list.append(our_list[rando])


# then remove the correct answer from our list of possibilies

our_list.remove(our_list[rando])

# shuffle the order of the list so the index values
# are not always in the same positions

random.shuffle(our_list)

# randomly select next item

rando = randint(0, len(our_list)-1)
answer_list.append(our_list[rando])

# now there are two items in the answer list

# remove second answer

our_list.remove(our_list[rando])

random.shuffle(our_list)

# randomly select last / third item

rando = randint(0, len(our_list)-1)
answer_list.append(our_list[rando])

print(answer_list)
'''