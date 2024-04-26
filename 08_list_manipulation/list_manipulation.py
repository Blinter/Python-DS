def list_manipulation(lst, command, location, value=None):
    """Mutate list to add/remove from beginning or end.

    - list: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if  (command.lower() != 'add' and command.lower() != 'remove') \
        or (location.lower() != 'beginning' and location.lower() != 'end') \
        or len(lst) <= 0 \
        or (value is None and command.lower() == 'add'):
        return None
    if command.lower() == 'add':
        if location.lower() == 'beginning':
            lst.insert(0, value)
            return lst
        # elif location.lower() == 'end':
        lst.append(value)
        return lst;
    #elif command.lower() == 'remove':
    if location.lower() == 'beginning':
        return lst.pop(0)
        # else: # elif location.lower() == 'end':
    return lst.pop()