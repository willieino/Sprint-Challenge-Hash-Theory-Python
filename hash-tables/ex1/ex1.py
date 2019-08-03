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

    #calculate values we need so subtract the weight from 21 to get value
    #new_indexes = []

    #for weight in weights:
    #    weight_match = limit - weight
    #    new_indexes.append(weight_match)
    #    #print(weight_match)
    #    #print(new_indexes)

    #for weight in weights:
        
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    #print(ht)
    answer = []
    found = False
    count = 0
    for i in range(0, length):
        value = hash_table_retrieve(ht,weights[i])
        weight_match = limit - weights[i]
        #print(value)
        for j in range(0, length):
            if weight_match == weights[j]:
                if j > i:
                    answer.append(j)
                    answer.append(i)
                else:
                     answer.append(i)
                     answer.append(j) 
                #print_answer(answer)
                return answer
    answer = None    
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

#new_weights = [ 4, 6, 10, 15, 16 ] 
#new_length = 5 
#new_limit = 21
#get_indices_of_item_weights(new_weights, new_length, new_limit)