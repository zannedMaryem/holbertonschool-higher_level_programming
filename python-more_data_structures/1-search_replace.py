#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list.copy()
    for element in my_list:
        pos = my_list.index(search)
        list[pos] = replace
    return list

