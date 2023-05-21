# PART A
"""
Q1
"""

def fibonacci_chars(n, k):
    fib_memo = {0: 'a', 1: 'bc'}

    def get_fib(n):
        if n not in fib_memo:
            fib_memo[n] = get_fib(n - 2) + get_fib(n - 1)
        return fib_memo[n]

    return get_fib(n)[k]


# PART B
"""
Q2
"""


def drainage_basins(elevation_histogram):
    index_list = []
    EH = elevation_histogram

    if len(elevation_histogram) < 2:
        return []

    if EH[0] < EH[1]:
        index_list.append(0)

    checked = []

    def check_basin(left, right):
        checked.append((left, right))

        if right - left == 2:
            if EH[left] > EH[left + 1] and EH[right] > EH[left + 1] and EH[left + 1]:
                index_list.append(left + 1)

        else:
            if (left, right - 1) not in checked:
                # ignore right & check left n-1
                check_basin(left, right - 1)
            if (left + 1, right) not in checked:
                # ignore left & check right n-1
                check_basin(left + 1, right)

    check_basin(0, len(EH) - 1)

    if EH[-1] < EH[-2]:
        index_list.append(len(EH) - 1)

    return index_list


# PART C
"""
Q1
"""


def is_legit_track(grid, i1, j1, i2, j2, current_weight):

    # checking if movement direction is legal, and if starting weight is legal
    move_is_legal = (i2 - i1 == 1 and j2 - j1 != 1) or (i2 - i1 != 1 and j2 - j1 == 1) \
                        or (i1 - i2 == 1 and j1 - j2 != 1) or (i1 - i2 != 1 and j1 - j2 == 1)

    if not move_is_legal or (current_weight > 0 and current_weight >= grid[i1][j1] * 2):
        return False
    # checking if weight after movement is legal
    if current_weight + grid[i2][j2] < grid[i2][j2] * 2:
        return True
    return False


"""
Q2
"""


def get_number_legit_tracks(grid, i1, j1):
    # recursion: progress legally, until reaching the end
    # count number of successful paths

    # MINI problem: next to end cell. move to there.
    # if 2 cells away, move to one cell away.

    def move_from(i1, j1, current_weight, successful_paths):
        # stop-conditions
        end_i, end_j = len(grid) - 1, len(grid[-1]) - 1
        if i1 == end_i and j1 == end_j:
            successful_paths += 1

        # move right
        if j1 != end_j and is_legit_track(grid, i1, j1, i1, j1 + 1, current_weight):
            weight_after_right = current_weight + grid[i1][j1 + 1]
            successful_paths = move_from(i1, j1 + 1, weight_after_right, successful_paths)

        # move down
        if i1 != end_i and is_legit_track(grid, i1, j1, i1 + 1, j1, current_weight):
            weight_after_down = current_weight + grid[i1 + 1][j1]
            successful_paths = move_from(i1 + 1, j1, weight_after_down, successful_paths)

        # move left
        if j1 != 0 and is_legit_track(grid, i1, j1, i1, j1 - 1, current_weight):
            weight_after_right = current_weight + grid[i1][j1 - 1]
            successful_paths = move_from(i1, j1 - 1, weight_after_right, successful_paths)

        # move up
        if i1 != 0 and is_legit_track(grid, i1, j1, i1 - 1, j1, current_weight):
            weight_after_down = current_weight + grid[i1 - 1][j1]
            successful_paths = move_from(i1 - 1, j1, weight_after_down, successful_paths)

        return successful_paths

    return move_from(i1, j1, grid[i1][j1], 0)


# PART D
"""
Q1
"""

def optimize_flowers_selection(flowers, budget):
    if budget < 0:
        return float('-inf'), 0
    if len(flowers) == 0:
        return 0, budget

    not_chosen = optimize_flowers_selection(flowers[1:], budget)
    chosen = optimize_flowers_selection(flowers[1:], budget - flowers[0][2])
    chosen = (chosen[0] + flowers[0][1], chosen[1])

    if not_chosen > chosen:
        return not_chosen
    else:
        return chosen


"""
Q2
"""


def get_plants_to_buy_faster(flowers, budget):
    def choose_flowers_memoed(flower_list, budget, memo_dict):

        # returns: value, budget
        if budget < 0:
            return float('-inf'), 0
        if len(flower_list) == 0:
            return 0, budget

        key = tuple(flower_list), budget

        if key not in memo_dict:
            not_chosen = choose_flowers_memoed(flower_list[1:], budget, memo_dict)
            chosen = choose_flowers_memoed(flower_list[1:], budget - flower_list[0][2], memo_dict)
            chosen = (chosen[0] + flower_list[0][1], chosen[1])

            if not_chosen > chosen:
                memo_dict[key] = not_chosen
            else:
                memo_dict[key] = chosen

        return memo_dict[key]

    return choose_flowers_memoed(flowers, budget, {})


