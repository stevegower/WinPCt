def record_pct(A):
    """
    Input:
        list (list of tuples) - list of tuples of record percents

    Returns:
        record_pct (integer) - record percentage
    """
    middle = list()
    for i in range(len(A)):
        possible = 1
        for j in range(len(A[i])):
            possible *= A[i][j]
        middle.append(possible)
    record_pct = 0
    for i in range(len(middle)):
        record_pct += middle[i]
    return record_pct