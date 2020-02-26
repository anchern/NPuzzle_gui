from constants import FIELD_SIZE
from random import randint

numbers = [i for i in range(FIELD_SIZE ** 2)]
field_map = [['0'] * FIELD_SIZE for i in range(FIELD_SIZE)]
solution_map = [['0'] * FIELD_SIZE for i in range(FIELD_SIZE)]
end_game = False


def fill_map():
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if len(numbers) == 1:
                field_map[i][j] = str(numbers[0])
            else:
                elem_number = randint(0, len(numbers) - 1)
                field_map[i][j] = str(numbers[elem_number])
                numbers.pop(elem_number)


def fill_map_solution():
    global solution_map
    i, j, k = 0, 0, 1
    while k < FIELD_SIZE ** 2:
        while j < FIELD_SIZE and solution_map[i][
            j] == '0' and k < FIELD_SIZE ** 2:
            solution_map[i][j] = str(k)
            k += 1
            j += 1
        j -= 1
        i += 1
        while i < FIELD_SIZE and solution_map[i][
            j] == '0' and k < FIELD_SIZE ** 2:
            solution_map[i][j] = str(k)
            k += 1
            i += 1
        i -= 1
        j -= 1
        while j >= 0 and solution_map[i][j] == '0' and k < FIELD_SIZE ** 2:
            solution_map[i][j] = str(k)
            k += 1
            j -= 1
            if j >= FIELD_SIZE:
                break
        j += 1
        i -= 1
        while i >= 0 and solution_map[i][j] == '0' and k < FIELD_SIZE ** 2:
            solution_map[i][j] = str(k)
            k += 1
            i -= 1
        i += 1
        j += 1


def print_field():
    print('\n'.join(str(f) for f in field_map))


def get_elem_index(elem):
    i = None
    j = None
    for i, sublist in enumerate(field_map):
        if elem in sublist:
            j = sublist.index(elem)
            break
    return i, j


def swap(i, j, k, l):
    field_map[i][j], field_map[k][l] = field_map[k][l], field_map[i][j]


def is_equal_maps():
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if field_map[i][j] != solution_map[i][j]:
                return False
    return True


def is_moved(elem):
    global end_game
    index_elem = get_elem_index(elem)
    index_free_elem = get_elem_index('0')
    dif = [0, 0]
    for i in range(2):
        dif[i] = abs(index_elem[i] - index_free_elem[i])
    if (dif[0] == 1 and dif[1] == 0) or (dif[1] == 1 and dif[0] == 0):
        if dif[0] - dif[1] == 0:
            return False
        swap(*index_elem, *index_free_elem)
        if is_equal_maps():
            end_game = True
        return True
    return False


if __name__ == '__main__':
    fill_map()
    print_field()
    # print(is_moved('11'))
    # print_field()
    # print('\n'.join(f for f in field_map))
