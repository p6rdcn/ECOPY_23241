# P6RDCN


# 1. feladat
def evens_from_list(input_list):
    new_list = []
    for i in input_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


# 2. feladat
def every_element_is_odd(input_list):
    odd_list = []
    for i in input_list:
        if i % 2 == 0:
            return False
        else:
            odd_list.append(i)
        if len(odd_list) == len(input_list):
            return True


# 3. feladat
def kth_largest_in_list(input_list, kth_largest):
    ordered_list = sorted(input_list)
    return ordered_list[-kth_largest]


# 4. feladat
def cumavg_list(input_list):
    new_list = []
    for i in range(len(input_list)):
        new_list.append(sum(input_list[0:i+1])/len(input_list[0:i+1]))
    return new_list


# 5. feladat
def element_wise_multiplication(input_list1, input_list2):
    new_list = []
    if len(input_list1) < len(input_list2):
        shorter_list = input_list1
    else:
        shorter_list = input_list2
    for i in range(len(shorter_list)):
        new_list.append(input_list1[i] * input_list2[i])
    return new_list


# 6. feladat
def merge_lists(*lists):
    new_list = []
    for i in lists:
        for j in i:
            new_list.append(j)
    return new_list


# 7. feladat
def squared_odds(input_list):
    new_list = []
    for i in input_list:
        if i % 2 == 1:
            new_list.append(i**2)
    return new_list


# 8. feladat
def reverse_sort_by_key(input_dict):
    keys = list(reversed(sorted(input_dict)))
    new_dict = {}
    for i in keys:
        new_dict[i] = input_dict[i]
    return new_dict


# 9. feladat
def sort_list_by_divisibility(input_list):
    new_dict = {}
    by_two = []
    by_five = []
    by_two_and_five = []
    by_none = []

    for i in input_list:
        if i % 2 == 0:
            if i % 5 == 0:
                by_two_and_five.append(i)
            else:
                by_two.append(i)
        elif i % 5 == 0:
            by_five.append(i)
        else:
            by_none.append(i)

    new_dict["by_two"] = by_two
    new_dict["by_five"] = by_five
    new_dict["by_two_and_five"] = by_two_and_five
    new_dict["by_none"] = by_none
    return new_dict