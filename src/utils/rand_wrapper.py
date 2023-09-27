import random
random.seed(42)


def random_from_list(input_list):
    return input_list[random.randint(0, len(input_list)-1)]


def random_sublist_from_list(input_list, number_of_elements):
    return random.choices(input_list, k = number_of_elements)
# def random_sublist_from_list(input_list, number_of_elements):
#     return [random.sample(input_list, number_of_elements)]
# def random_sublist_from_list(input_list, number_of_elements):
#     return [input_list.pop(random.randint(0, len(input_list)-1)) for i in range(number_of_elements)]


def random_from_string(input_string):
    return random.choice(input_string)


def hundred_small_random():
    return [random.random() for i in range(100)]


def hundred_large_random():
    return [random.randint(10, 1000) for i in range(100)]


def five_random_number_div_three():
    new_list = [x for x in range(9, 1000) if x % 3 == 0]
    return random.sample(new_list, 5)
# def five_random_number_div_three():
#     new_list = []
#     while len(new_list) < 5:
#         a = random.randint(9, 1000)
#         if a % 3 == 0:
#             new_list.append(a)
#         else:
#             continue
#     return new_list


def random_reorder(input_list):
    return random.sample(input_list, len(input_list))
# def random_reorder(input_list):
#     random.shuffle(input_list)
#     return input_list


def uniform_one_to_five():
    return random.uniform(1, 6)