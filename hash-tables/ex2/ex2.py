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
   
    for i in range(length):
        # retrieve a ticket from hash table
        found = False
        count = 0
        while found is False:
            print("Count: ", count)
            destination = hash_table_retrieve(hashtable, tickets[count].source)
            print(destination)
            print(tickets[count].source)
            
            if tickets[count].source == "NONE":
                found = True
                route.append(destination)
            count += 1
        print("Got the first card")
        
        return
        # so we have the first card.

        # search tickets until the source = None
        # so this is the first card
    
        # Loop through the cards
        # compare the current destination to the rest of the cards sources  
        # until i find a match
        
        # a match means its the next card so append it to our temp array

        # make it our current source and repeat the loop





    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
length = 2
tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, length)