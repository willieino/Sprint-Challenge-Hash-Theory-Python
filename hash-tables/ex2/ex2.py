#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination




def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
# starting location is the key
# destination is the value
# the ith location in the route can be found by checking the hash table for the i-1th location.

#        ticket_1 = Ticket("NONE", "PDX")
#        ticket_2 = Ticket("PDX", "DCA")
#        ticket_3 = Ticket("DCA", "NONE")

#        tickets = [ticket_1, ticket_2, ticket_3]
    route = []
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    found = False
    count = 0
    source = ""
    while found is False:       
        destination = hash_table_retrieve(hashtable, tickets[count].source)       
        if tickets[count].source == "NONE":
            found = True
            route.append(destination)
            source = destination
        count += 1
    count = 0
    found = False
    
    while found is False:      
        destination = hash_table_retrieve(hashtable, tickets[count].source)
        if source == tickets[count].source:        
            route.append(destination)
            if destination == "NONE":
                return route
            source = destination
            count = 0         
        elif source == "NONE":       
            return route
        else:
            count += 1
    return route


