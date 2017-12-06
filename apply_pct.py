def apply_pct(record_list, win_pct):
    """
    Inputs:
        record_list (binary list) - list containing wins (1) and losses (0) in every possible unique permutation
        win_pct (list) - list containing win percentage to be applied

    Returns:
        pcts_applied (list) - list with win/loss percentages applied
    """
    def bin_helper(tupleA, listB):
        """
        Inputs:
            tupleA (tuple) - tuple of objects
            listB (list of same length as tuple) - list of objects to apply
        
        Returns:
            tupleB (tuple) - tuple of applied objects
        """
        empty = list()
        for i in range(len(tupleA)):
            if tupleA[i] == 1:
                empty.append(listB[i])
            elif tupleA[i] == 0:
                empty.append((1 - listB[i]))
            else:
                pass
        return tuple(empty)

    pcts_applied = list()
    for i in range(len(record_list)):
        pcts_applied.append(bin_helper(record_list[i], win_pct))
    return pcts_applied