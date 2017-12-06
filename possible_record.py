def possible_records(games):
    """
    Input:
        games (integer) - number of games played

    Returns:
        records (list of tuples) - list of possible records as tuples
    """
    records = list()
    for i in range(games + 1):
        records.append((i, games-i))
    return records