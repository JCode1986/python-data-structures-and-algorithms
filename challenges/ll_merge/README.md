# Merge linked lists
Merge two linked lists.

## Challenge Description
Write a function called `merge_lists` which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Approach & Efficiency
* Return first linked list if second linked list is not preset, and vice versa
* while loop to traverse through both linked lists
* Store both linked list's next for reference
* Re-assign first linked list's head to second linked list's head
* Have condition to add the rest of the nodes of the linked list if one linked list is short than the other.  

O(n)

## Solution
![enter name here](./image/array-shift.jpeg)
