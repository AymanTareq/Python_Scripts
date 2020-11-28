def find_max(lst):
    # This function is for finding max value form a list.
    max = lst[0]
    for number in lst:
        if number > max:
            max = number
    return max