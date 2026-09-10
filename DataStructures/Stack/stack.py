from DataStructures.List import single_linked_list as sl

def new_stack ():
    pila= sl.new_list()
    return pila

def push(my_stack, element):
    stack= sl.add_first(my_stack, element)
    return stack

def pop(my_stack):
    elemento= sl.remove_first(my_stack)
    return elemento

def is_empty(my_stack):
    return sl.is_empty(my_stack)

def top(my_stack):
    elemento= sl.first_element(my_stack)
    return elemento

def size(my_stack):
    return sl.size(my_stack)
