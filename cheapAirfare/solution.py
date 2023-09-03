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

'''Function to get the lowest round if exist , else it will return [1000000, -1, -1]'''
def getLowestRoundTrip(cost_matrix):
    #initializing the lowest_trip with a data which is said to be return 
    #if there is no round trip exist 
    lowest_trip = [1000000, -1, -1]
    '''The loops are defined to ensure we are only iterating for minimal number 
    [
     *  *   *   *
     5  *   *   *
     9  10  *   *
     13 14  15  *
     ]
    '''
    inner_index = 1
    for i in range (1, len(cost_matrix)):
        for j in range(inner_index):
            if ((x:=cost_matrix[i][j]) != -1 and (y:=cost_matrix[j][i]) != -1):
                if (total_cost:=x + y) < lowest_trip[0]:
                    lowest_trip = [total_cost] + sorted([i, j])
        inner_index += 1
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
