def contains_values(input_list, element):
    return(element in input_list)

def number_of_elements_in_list(input_list):
    return len(input_list)

def remove_every_element_from_list(input_list):
    input_list.clear()
    return None



def reverse_list(input_list):
    return list(reversed(input_list))

def odds_from_list(input_list):
    odd_elements = []
    for i in input_list:
        if i % 2 == 1:
            odd_elements.append(i)
    return odd_elements

def number_of_odds_in_list(input_list):
    odd_elements = []
    for i in input_list:
        if i % 2 == 1:
            odd_elements.append(i)
    return len(odd_elements)

def contains_odd(input_list):
    odd_elements = []
    for i in input_list:
        if i % 2 == 1:
            odd_elements.append(i)
    if len(odd_elements) > 0:
        return True
    else:
        return False

def second_largest_in_list(input_list):
    ordered_list = sorted(input_list)
    return ordered_list[-2]

def sum_of_elements_in_list(input_list):
    return sum(input_list)

def cumsum_list(input_list):
    summing_list = []
    summing = 0
    for i in input_list:
        summing = summing + i
        summing_list.append(summing)
    return summing_list

def element_wise_sum(input_list1, input_list2):
    new_list = []
    if len(input_list1) < len(input_list2):
        shorter_list = input_list1
    else:
        shorter_list = input_list2
    for i in range(len(shorter_list)):
        new_list.append(input_list1[i] + input_list2[i])
    return new_list

def subset_of_list(input_list, start_index, end_index):
    return input_list[start_index:end_index+1]

def every_nth(input_list, step_size):
    new_list = []
    length = len(input_list)
    counter = 0
    while counter <= length-1:
        new_list.append(input_list[counter])
        counter = counter + step_size
    return new_list

def only_unique_in_list(input_list):
    new_list = []
    for i in input_list:
        if i in new_list:
            return False
        else:
            new_list.append(i)
    return True

def keep_unique(input_list):
    new_list = []
    for i in input_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

def swap(input_list, first_index, second_index):
    new_list = []
    counter = 0
    for i in input_list:
        if counter == first_index:
            new_list.append(input_list[second_index])
        elif counter == second_index:
            new_list.append(input_list[first_index])
        else:
            new_list.append(i)
        counter = counter + 1
    return new_list

def remove_element_by_value(input_list, value_to_remove):
    new_list = []
    for i in input_list:
        if i == value_to_remove:
            continue
        else:
            new_list.append(i)
    return new_list

def remove_element_by_index(input_list, index):
    new_list = []
    counter = 0
    for i in input_list:
        if counter != index:
            new_list.append(i)
        counter = counter + 1
    return new_list

def multiply_every_element(input_list, multiplier):
    new_list = []
    for i in input_list:
        new_list.append(i * multiplier)
    return new_list



### DICTIONARIES

def remove_key(input_dict, key):
    if key in input_dict:
        del input_dict[key]
    return input_dict

def sort_by_key(input_dict):
    keys = sorted(input_dict)
    new_dict = {}
    counter = 0
    for i in keys:
        print("counter: " + str(counter))
        new_dict[i] = input_dict[i]
    return new_dict

def sum_in_dict(input_dict):
    new_list = []
    for i in input_dict:
        new_list.append(input_dict[i])
    return sum(new_list)

def merge_two_dicts(input_dict1, input_dict2):
    merged_dict = {}
    for i in input_dict1:
        merged_dict[i] = input_dict1[i]
    for j in input_dict2:
        merged_dict[j] = input_dict2[j]
    return merged_dict

def merge_dicts(*dicts):
    merged_dict = {}
    for i in dicts:
        for j in i:
            merged_dict[j] = i[j]
    return merged_dict

def sort_list_by_parity(input_list):
    parity_dict = {}
    even_list = []
    odd_list = []
    for i in input_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    parity_dict["odd"] = odd_list
    parity_dict["even"] = even_list
    return parity_dict

def mean_by_key_value(input_dict):
    new_dict = {}
    for i in input_dict:
        new_dict[i] = sum(input_dict[i])/len(input_dict[i])
    return new_dict

def count_frequency(input_list):
    new_dict = {}
    for i in input_list:
        if i in new_dict:
            new_dict[i] = new_dict[i] + 1
        else:
            new_dict[i] = 1
    return new_dict