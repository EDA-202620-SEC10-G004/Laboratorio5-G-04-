
from DataStructures.List import array_list as lt
def new_queue ():
    queue = lt.new_list()
    return queue
def enqueue (my_queue, element):
    cola = lt.add_last(my_queue, element)
    return cola
def dequeue (my_queue):
    eliminado= lt.remove_first(my_queue)
    return eliminado
def peek (my_queue):
    primero= lt.first_element(my_queue)
    return primero
def is_empty(my_queue):
    vacio= lt.is_empty(my_queue)
    return vacio
def size(my_queue):
    tamano= lt.size(my_queue)
    return tamano