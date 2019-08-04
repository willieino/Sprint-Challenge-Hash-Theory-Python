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
        weight_match = limit - weights[i]  
        for j in range(length):
            if weight_match == weights[j]:
                if j > i:
                    answer = tuple((j, i))   
                    return answer
                elif j < i:
                    answer = tuple((i, j))  
                    return answer           
    answer = None    
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

