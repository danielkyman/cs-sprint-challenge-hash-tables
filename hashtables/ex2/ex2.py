#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    sourceTicket = None
    ticketsMap = {}

    for i in range(length):
        if tickets[i].source == 'NONE':
            sourceTicket = tickets[i]
        else:
            ticketsMap[tickets[i].source] = tickets[i].destination

    # start route with destination of startRoute and traverse through map to find ultimate destination
    flying = True
    route = []
    pointer = sourceTicket.destination
    while flying:
        route.append(pointer)
        if ticketsMap[pointer] == 'NONE':
            flying = False
            route.append('NONE')
        else:
            pointer = ticketsMap[pointer]

    return route
