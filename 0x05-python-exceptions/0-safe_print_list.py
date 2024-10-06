#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elememts of a list.

    Args:
    my_list (list): The list to print elements from.
    x (int): The number of elements in my_list to be printed.

    Returns:
    The number of elements printed.
    """
    num = 0
    for i in range(x):
    try:
    print("{}".format(my_list[i]), end="")
    num += 1
    except IndexError:
    break
    print("")
    return (num)
