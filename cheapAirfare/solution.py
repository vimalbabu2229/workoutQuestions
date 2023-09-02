'''Function to find the cost matrix assuming that a value of -1 
between two nodes means there is no edge between them'''
def getCostMatrix(input_data):
    # initializing the items  in const matrix with a -1 , indicating there is no
    # edge between the indices .
    cost_matrix = [[-1]*input_data[0] for i in range(input_data[0])]
    # updating the known values of cost
    for x in (input_data[2:]):
        cost_matrix[x[0]][x[1]] = x[2]
    # deriving the unknown values of cost
    # using dijkstra's algorithm
    for i in range(input_data[0]):
        for j in range(input_data[0]):
            for k in range(input_data[0]):
                if cost_matrix[i][k] != -1 and cost_matrix[k][j] != -1:
                    temp = cost_matrix[i][k] + cost_matrix[k][j]
                    cost_matrix[i][j] = temp if 0 < temp < cost_matrix[i][j] else cost_matrix[i][j]
    return cost_matrix

'''Below function checks a round trip exist (means there is a trip exist not only form 
source to destination but also vice versa), and if exist it return the list containing the 
total price as the first item , then the nodes (source and destination ) in ascending order '''
def getRoundIfExist(cost_matrix, source, destination):
    if (x:=cost_matrix[source][destination]) != -1 and (y:=cost_matrix[destination][source]) != -1:
        total_cost = x + y
        return [total_cost, min(source, destination), max(source, destination)]
    return [1000000, -1, -1]

'''Below function calls the getRoundIfExist() to get the result for a single pair of 
source abd destination and update the lowest_trip variable accordingly '''
def getLowestRoundTrip(cost_matrix):
    #initializing the lowest_trip with a data which is said to be return 
    #if there is no round trip exist 
    lowest_trip = [1000000, -1, -1]
    for i in range (len(cost_matrix)):
        for j in range(len(cost_matrix)):
            if i != j and (x:=getRoundIfExist(cost_matrix, i, j))[0] < lowest_trip[0]:
                lowest_trip = x
    return lowest_trip

if __name__ == "__main__":
    '''Sample input 0'''
    input_data = [
        4, 6,
        [0, 1, 20],
        [1, 0, 20],
        [1, 2, 10],
        [2, 0, 10],
        [1, 3, 30],
        [3, 2, 30]
    ]
    '''sample input 1'''
    # input_data = [
    #     3, 
    #     3, 
    #     [0, 1, 100],
    #     [1, 2, 100],
    #     [0, 2, 100]
    # ]
    cost_matrix = getCostMatrix(input_data)
    lowest_round_trip = getLowestRoundTrip(cost_matrix)

    print(lowest_round_trip)
