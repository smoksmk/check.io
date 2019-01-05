def who_win(s):
    if s[0] != '.' and s.strip(s[0]) == '':
        return s[0]

def checkio(result):
    length = len(result)

    # rows:
    to_check = result
    # diagonal:
    to_check.append(''.join(result[i][i] for i in range(length)))
    # reverse diagonal:
    to_check.append(''.join(result[i][-i-1] for i in range(length)))
    # collumns:
    to_check += [''.join(result[i][j] for i in range(length))
                         for j in range(length)]

    for res in to_check:
        won = who_win(res)
        if won:
            return won

    # anyway, draw
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

