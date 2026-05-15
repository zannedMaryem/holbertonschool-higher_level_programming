#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    new_list = list(my_set)
    my_sum = 0
    for i in range(len(new_list)):
        my_sum += new_list[i]
    return my_sum
