def main(win_pct):
    """
    Inputs:
        win_pct (list) - list of win percentages from each week

    Returns:
        Projected Records for All Possible Wins
    """
    from games import calc_games
    games = calc_games(win_pct)
    from possible_record import possible_records
    records = possible_records(games)
    from record_list import record_list
    from apply_pct import apply_pct
    from record_pct import record_pct
    print('Percentages for All Possible Records')
    for record in records:
        print('{} - {} ...'.format(record[0], record[1]), end=' ')
        record_L = record_list(games, record[0])
        applied = apply_pct(record_L, win_pct)
        print(str(round(record_pct(applied)*100, 2)) + "%")
    
    

