import sys

WIN = 0
LOSS = 1
UNDECIDED = 2

result_to_string = {
    WIN: 'Win',
    LOSS: 'Loss',
    UNDECIDED: 'Undecided',
}

def main():
    init_pos = 4
    result = solve(init_pos)
    print(result_to_string[result])

def primitive(pos):
    if pos == 0:
        return LOSS
    return UNDECIDED

def generate_moves(pos):
    if pos >= 1:
        yield -1
    if pos >= 2:
        yield -2

def do_move(pos, move):
    return pos + move

def solve(current_pos):
    result = primitive(current_pos)
    if result != UNDECIDED:
        return result
    all_wins = True
    for move in generate_moves(current_pos):
        new_pos = do_move(current_pos, move)
        new_result = solve(new_pos)
        if new_result == LOSS:
            return WIN
        if new_result != WIN:
            all_wins = False
    if all_wins:
        return LOSS

if __name__ == '__main__':
    main()