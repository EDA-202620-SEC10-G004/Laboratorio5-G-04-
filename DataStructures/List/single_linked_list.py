from DataStructures.List import list_node as node 

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist

def add_first(my_list, element):
    new_node = node.new_single_node(element)

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node

    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = node.new_single_node(element)

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node

    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["first"]["info"]

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["last"]["info"]

def is_empty(my_list):
    return my_list["size"] == 0

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]

    while searchpos < pos:
        node = node["next"]
        searchpos += 1

    return node["info"]

def remove_first(my_list):
    if my_list["size"] == 0:
        return None

    element = my_list["first"]["info"]

    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        my_list["first"] = my_list["first"]["next"]

    my_list["size"] -= 1

    return element

def remove_last(my_list):
    if my_list["size"] == 0:
        return None

    element = my_list["last"]["info"]

    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        current = my_list["first"]

        while current["next"] != my_list["last"]:
            current = current["next"]

        current["next"] = None
        my_list["last"] = current

    my_list["size"] -= 1

    return element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        return None

    if pos == 0:
        return add_first(my_list, element)

    if pos == my_list["size"]:
        return add_last(my_list, element)

    new_node = node.new_single_node(element)

    current = my_list["first"]
    current_pos = 0

    while current_pos < pos - 1:
        current = current["next"]
        current_pos += 1

    new_node["next"] = current["next"]
    current["next"] = new_node
    my_list["size"] += 1

    return my_list

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0

    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1

    return count

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return None

    if pos == 0:
        remove_first(my_list)
        return my_list

    if pos == my_list["size"] - 1:
        remove_last(my_list)
        return my_list

    previous = my_list["first"]
    current_pos = 0

    while current_pos < pos - 1:
        previous = previous["next"]
        current_pos += 1

    previous["next"] = previous["next"]["next"]
    my_list["size"] -= 1

    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        return None

    current = my_list["first"]
    current_pos = 0

    while current_pos < pos:
        current = current["next"]
        current_pos += 1

    current["info"] = new_info

    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"]:
        return None

    if pos2 < 0 or pos2 >= my_list["size"]:
        return None

    node1 = my_list["first"]
    node2 = my_list["first"]

    current_pos = 0
    while current_pos < pos1:
        node1 = node1["next"]
        current_pos += 1

    current_pos = 0
    while current_pos < pos2:
        node2 = node2["next"]
        current_pos += 1

    node1["info"], node2["info"] = node2["info"], node1["info"]

    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or num_elements < 0 or pos + num_elements > my_list["size"]:
        return None

    sublist = new_list()
    current = my_list["first"]

    for _ in range(pos):
        current = current["next"]

    for _ in range(num_elements):
        add_last(sublist, current["info"])
        current = current["next"]

    return sublist
def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def selection_sort(my_list, sort_criteria):
    size = my_list["size"]

    for i in range(size - 1):
        minimum = i

        for j in range(i + 1, size):
            if sort_criteria(
                get_element(my_list, j),
                get_element(my_list, minimum)
            ):
                minimum = j

        if minimum != i:
            exchange(my_list, i, minimum)

    return my_list


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted