def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length == 2 and (weights[0] + weights[1] == limit):
        return [1, 0]
    if length > 2:
        # hash the weights
        weightsHash = {}
        for i in range(length):
            print(weightsHash)
            weightsHash[weights[i]] = i

        for i in range(length):
            weight1 = weights[i]
            if limit > weight1:
                weight2 = limit - weight1
                if weight2 in weightsHash:
                    if weightsHash[weight2] > i:
                        return [weightsHash[weight2], i]
                    else:
                        return [i, weightsHash[weight2]]
            print(weightsHash)
    return None
