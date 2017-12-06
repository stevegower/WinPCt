def record_list(games, wins):
    """
    Inputs:
        games (integer) - total number of games played
        wins (integer <= games) - total number of games won

    Returns:
        record_list (list) - all possible ways record could be achieved as binary
    """
    import itertools
    record = list()
    losses = games - wins
    for i in range(wins):
        record.append(1)
    for i in range(losses):
        record.append(0)
    record_list = list(set(itertools.permutations(record)))
    return record_list