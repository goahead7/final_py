from functools import reduce

# если на вход подавать строку
# def fill(elem):
#     return list(dict.fromkeys(map(int, elem.split(","))))


# если на вход список, удаление повторяющихся элементов списка
def fill(list_1):
    return list(dict.fromkeys(list_1))


# принадлежность каждого 3-ьего эл-та 1-го мн-ва ко второму и !принадлежность каждого 2-го эл-та 2-го к 1-му
def compare(num_1, num_2):
    return print(set(fill(num_1)[2::3]).issubset(fill(num_2)) and (not set(fill(num_2)[1::2]).issubset(fill(num_1))))


# добавление четных элементов первого множества ко второму
def even(num_1, num_2):
    return list(dict.fromkeys(fill(num_2) + [x for x in fill(num_1) if x % 2 == 0]))


# длина множества
def len_list(num):
    return len(fill(num))


# минимальный элемент множества, элемент меньше заданного числа
def min_list(num, y):
    return min([x for x in fill(num) if x < y])


# макс из второго, который меньше макс из первого
def max_min(num_1, num_2):
    return max([x for x in fill(num_2) if x < max(fill(num_1))])


# сумма всех больше заданного
def sum_list(num, y):
    return reduce(lambda acc, x: acc + (x if x > y else 0), fill(num), 0)


if __name__ == "__main__":
    print(fill([1, 2, 3, 4, 5, 5, -1, 2, -5, 2]))
    print(even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [12, 10, 3, 4, 5, 6, 3, 19, 18, -11, -11]))
    print(len_list([12, 10, 3, 4, 5, 6, 3, 19, 18, -11, -11]))
    print(min_list([1, 2, 3, 4, 5, 5, -1, 2, -5, 2], 2))
    print(max_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [12, 10, 3, 4, 5, 6, 3, 19, 18, -11, -11]))
    print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
