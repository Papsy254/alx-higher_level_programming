#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list in my_list that are integers.

    Args:
        my_list (list): Contaiins integers to be printed.
        x (int): The number of elements of my_list to be printed.

    Returns:
        The number of elements printed.
    """
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
