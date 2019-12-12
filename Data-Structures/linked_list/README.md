# Singly Linked List

## Challenge
* Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
* Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
* Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
* Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
* Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List.

## Approach & Efficiency
* `insert` method - O(1); always to the head
* `includes` method - O(n); possibly traverses through entire linked list
* `to_string` method - O(n); traverses through entire linked list
* `append(value)` medthod - O(1) always at end of list
* `insertBefore(value, newVal)` - O(n)
* `insertAfter(value, newVal)` - O(n)
* `kth_from_end(k)` - O(2n)
* `merge_lists(list1, list2)` - O(n)
## API
* `Class Node` with value and next attributes
* `Class_linked` list with head
    * `insert(value)` method - takes in a value as an argument, and inserts that that value into the head of the linked list
    * `includes(value)` method - takes in a value as an argument, and returns a boolean if the value is present or not in the linked list
    * `to_string` method - returns all the values in the linked list
    * `append(value)` which adds a new node with the given value to the end of the list
    * `insertBefore(value, newVal)` which add a new node with the given newValue immediately before the first value node
    * `insertAfter(value, newVal)` which add a new node with the given newValue immediately after the first value node
    * `kth_from_end(k)` - takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list.
    * `merge_lists(list1, list2)` - takes in two linked lists, zip the two linked list into one linked list