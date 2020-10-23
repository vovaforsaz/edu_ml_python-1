if __name__ == '__main__':
    print("lesson 2")
    """
    Lists and arrays:
    Lists are very similar to arrays. But lists are just like dynamic sized arrays. 
    They can contain any type of variable, and they can contain as many variables as you wish.
    For example list may contain DataTypes like Integers, Strings, as well as Objects. 
    Lists are mutable, and hence, they can be altered even after their creation. 


    List can be created by just placing the sequence inside the square brackets [].
    Unlike Sets, list doesn’t need a built-in function for creation of list.
    
    Main list methods:
    append() Add an element to the end of the list
    extend() Add all elements of a list to the another list
    insert() Insert an item at the defined index
    remove() Removes an item from the list
    pop() Removes and returns an element at the given index
    clear()	Removes all items from the list
    index()	Returns the index of the first matched item
    count()	Returns the count of number of items passed as an argument
    sort() Sort items in a list in ascending order
    reverse() Reverse the order of items in the list
    copy() Returns a copy of the list
    
    """

    my_list = [1, 2, 3, 4]
    print(my_list)

    # Accessing elements from the List
    print("Accessing element by index - ", my_list[2])

    # Accessing elements with negative indexing. Negative index represents positions from the end of the list.
    print("Accessing with negative index - ", my_list[-1])

    # Knowing the size of List
    print("Size of list - ", len(my_list))

    # append() - adding elements to a List
    my_list.append(100)
    my_list.append(200)
    my_list.append("hello")
    print(my_list)
    print("get first element of list - ", my_list[0])
    print("Size of list - ", len(my_list))

    # insert() - Insert element to the specific position. Method requires two arguments(position, value).
    my_list.insert(0, "new list element")
    print(my_list)

    # extend() - this method is used to add multiple elements at the same time at the end of the list.
    my_list.extend(["extend_1", "extend_2"])
    print(my_list)

    # remove() - Removing Elements from the List. Method removes only one element at a time.
    my_list.remove("hello")
    print(my_list)

    # pop() - Remove and return an element from the set
    print("Get and remove last element -", my_list.pop())
    print("Get and remove first element -", my_list.pop(0))
    print(my_list)

    # Slicing of a List
    new_list = ['l', 'e', 's', 'o', 'n', 'o', 'n', 'e']
    print("Sliced new_list - ", new_list[2:5])
    print("Sliced new_list - ", new_list[:5])
    print("Sliced new_list - ", new_list[5:])

    # Negative index List slicing
    print("Sliced new_list with negative index - ", new_list[-8:-3])
