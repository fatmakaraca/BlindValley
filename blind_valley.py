import sys


def get_input():
    file_name = sys.argv[1]
    with open(file_name, 'r') as f:
        input_file = f.readlines()
    input_lst = [line.split() for line in input_file]

    count_highs_bases = input_lst[:4]
    for i in range(len(count_highs_bases)):
        for j in range(len(count_highs_bases[i])):
            count_highs_bases[i][j] = int(count_highs_bases[i][j])

    initial_board = input_lst[4:]

    return count_highs_bases, initial_board


def create_empty_board():
    initial_board = get_input()[1]
    row = len(initial_board)
    column = len(initial_board[0])
    empty_board = []
    for i in range(row):
        empty_board.append([])
        for j in range(column):
            empty_board[i].append(' ')
    return empty_board


def find_left_cell(board, row, column):
    if column != 0:
        left_cell_coordinate = [row, (column - 1)]
        return left_cell_coordinate
    else:
        return None


def find_right_cell(board, row, column):
    if column != len(board[0]) - 1:
        right_cell_coordinate = [row, (column + 1)]
        return right_cell_coordinate
    else:
        return None


def find_above_cell(board, row, column):
    if row != 0:
        above_cell_coordinate = [row - 1, column]
        return above_cell_coordinate
    else:
        return None


def find_below_cell(board, row, column):
    if row != len(board) - 1:
        below_cell_coordinate = [row + 1, column]
        return below_cell_coordinate
    else:
        return None


def check_constraints(board):  # This function checks the conditions of the filled board.
    constraints = [[], [], [], []]

    count_highs_bases = get_input()[0]

    for row in board:
        number_of_h = 0
        number_of_b = 0
        for cell in row:
            if cell == 'H':
                number_of_h += 1
            if cell == 'B':
                number_of_b += 1
        constraints[0].append(number_of_h)
        constraints[1].append(number_of_b)

    for i in range(len(board[0])):
        number_of_h = 0
        number_of_b = 0
        for row in board:
            if row[i] == 'H':
                number_of_h += 1
            if row[i] == 'B':
                number_of_b += 1
        constraints[2].append(number_of_h)
        constraints[3].append(number_of_b)

    for j in range(len(count_highs_bases)):
        for k in range(len(count_highs_bases[j])):
            if count_highs_bases[j][k] == -1:

                continue
            else:
                if constraints[j][k] == count_highs_bases[j][k]:
                    continue

                else:
                    return False

    return True


def is_proper(board, row, column, val):  # This function checks the suitability of the operation performed on the grid.
    neighbors = []

    if find_above_cell(board, row, column) is not None:
        neighbors.extend(board[find_above_cell(board, row, column)[0]][find_above_cell(board, row, column)[1]])

    if find_left_cell(board, row, column) is not None:
        neighbors.extend(board[find_left_cell(board, row, column)[0]][find_left_cell(board, row, column)[1]])

    if find_right_cell(board, row, column) is not None:
        neighbors.extend(board[find_right_cell(board, row, column)[0]][find_right_cell(board, row, column)[1]])

    if find_below_cell(board, row, column) is not None:
        neighbors.extend(board[find_below_cell(board, row, column)[0]][find_below_cell(board, row, column)[1]])

    for neighbor in neighbors:

        if neighbor == ' ':
            continue

        elif neighbor == 'N':
            continue

        else:
            if neighbor == val:
                return False

    return True


def other_val(val):  # It returns what value will come to the cells that contain 'R' or 'D' in the grid
    if val == 'H':
        other_part_of_value = 'B'
    elif val == 'B':
        other_part_of_value = 'H'
    elif val == 'N':
        other_part_of_value = 'N'

    return other_part_of_value


def row_constraints(row, board):  # It checks if row meets the conditions.
    count_highs_bases = get_input()[0]
    row_h = count_highs_bases[0][row]
    row_b = count_highs_bases[1][row]
    board_row_h = 0
    board_row_b = 0

    if row_h == -1 and row_b == -1:
        return True

    for cell in board[row]:
        if cell == 'H':
            board_row_h += 1
        elif cell == 'B':
            board_row_b += 1

    if row_h == -1:
        return board_row_b == row_b
    elif row_b == -1:
        return board_row_h == row_h

    return board_row_h == row_h and board_row_b == row_b


def other_val_index(row, column, letter):  # It returns the indices of cells containing 'R' or 'D' in the grid
    if letter == 'L':
        other_value_index = row, column + 1
    elif letter == 'U':
        other_value_index = row + 1, column
    return other_value_index


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def blind_valley(board):
    initial_board = get_input()[1]
    for row in range(len(board)):
        for column in range(len(board[0])):
            letter = initial_board[row][column]
            if letter == 'L' or letter == 'U':
                if board[row][column] == ' ':
                    for val in ['H', 'B', 'N']:
                        other_row, other_column = other_val_index(row, column, letter)
                        if is_proper(board, row, column, val) and is_proper(board, other_row, other_column, other_val(val)):
                            board[row][column] = val
                            board[other_row][other_column] = other_val(val)

                            if is_board_full(board) and check_constraints(board):
                                return True

                            if blind_valley(board):
                                return True

                            board[row][column] = ' '  # backtracking
                            board[other_row][other_column] = ' '  # backtracking

                    return False
        if row_constraints(row, board) == False:
            return False
        else:
            continue

    return check_constraints(board)


def main():
    first_board = create_empty_board()
    file_name = sys.argv[2]
    with open(file_name,'w') as output_file:
        if blind_valley(first_board):
            for i, row in enumerate(first_board):
                line = ' '.join(cell for cell in row)
                if i != len(first_board) - 1:
                    output_file.write(line + '\n')
                else:
                    output_file.write(line)

        else:
            output_file.write("No solution!")


if __name__ == '__main__':
    main()


