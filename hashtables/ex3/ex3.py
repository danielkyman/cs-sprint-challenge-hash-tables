def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    # put all elements with their counts in dict
    counts = {}

    for values in arrays:
        for item in values:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

    # get all items with count same as number of elements in arrays
    for item in counts:
        if counts[item] == len(arrays):
            result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
