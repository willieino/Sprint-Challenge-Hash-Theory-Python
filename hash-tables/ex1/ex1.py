#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)




def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Example Values
    #weights = [ 4, 6, 10, 15, 16 ] 
    #length = 5 
    #limit = 21

    # store weight as the key
    # store list index as the value

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        value = hash_table_retrieve(ht, weights[i])
        # determine the weight that we need: subtract current weight from limit
        weight_match = limit - weights[i]  
        # not happy with this part
        for j in range(length):
            # check for a match
            if weight_match == weights[j]:
                # need to put the largest index first in the tuple
                if j > i:
                    # match found, return the answer in a tuple
                    answer = tuple((j, i))   
                    return answer
                elif j < i:
                    # match found, return the answer in a tuple
                    answer = tuple((i, j))  
                    return answer           
    answer = None    
    return answer

# ***********************************************************************************
# this part was frustrating because if I called this print_answer function it fails
# saying that it needs a string value, so i converted the values to strings
# but then the tests all fail because they are lookung for integer values 
# in the tuple but it prints correctly. 
# **********************************************************************************

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

